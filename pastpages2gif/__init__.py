import requests
import datetime
import images2gif
from email import utils
from StringIO import StringIO
from PIL import Image, ImageOps


def get_site(gif_path, site_slug, start_time, end_time,
    duration=0.5, verbose=False, max_width=600, max_height=1000):
    """
    Connects to the PastPages API and pulls images to
    be converted into a GIF.
    """
    # Verify that the arguments are acceptable.
    if not isinstance(gif_path, basestring):
        raise TypeError("GIF path must be a string.")
    if not isinstance(site_slug, basestring):
        raise TypeError("Site slug must be a string.")
    if not isinstance(start_time, datetime.datetime):
        raise TypeError("Start time must be a datetime object.")
    if not isinstance(end_time, datetime.datetime):
        raise TypeError("Start time must be a datetime object.")
    if not isinstance(duration, float):
        raise TypeError("Duration must be a float.")
    if not isinstance(verbose, bool):
        raise TypeError("Verbose must be a boolean object.")
    # Make sure that dates are no more than 2 days apart
    datediff = end_time - start_time
    if datediff > datetime.timedelta(days=2):
        raise ValueError("Start and end datetime cannot be greater than 2 days apart.")
    if datediff < datetime.timedelta(minutes=60):
        raise ValueError("Start time must be at least one hour before end time.")
    # Format the URL to request data from the PastPages API
    # Documentation: http://www.pastpages.org/api/docs/
    # Example: http://www.pastpages.org/api/beta/screenshots/?site__slug=xinhua&timestamp__gte=2013-01-01%2000:00&timestamp__lte=2013-01-01%2001:00:00
    base_url = 'http://www.pastpages.org/api/beta/screenshots'
    payload = {
        'site__slug': site_slug,
        'timestamp__gte': start_time.isoformat(),
        'timestamp__lte': end_time.isoformat(),
        'limit': 50,
    }
    # Make the request
    if verbose:
        print "Requesting data from PastPages API"
    r = requests.get(base_url, params=payload)
    if verbose:
        print r.url
    # Fetch all the images
    url_list = [o['crop'] for o in r.json()['objects'] if o['has_crop']]
    # Throw an error if you don't find any
    if not url_list:
        raise ValueError("No screenshots found.")
    # Fetch the images
    image_list = []
    length = len(url_list)
    for i, url in enumerate(url_list):
        if verbose:
            print "Fetching image %s/%s" % (i+1, length)
        r = requests.get(url)
        i = Image.open(StringIO(r.content))
        image_list.append(i)
    # Resize them so they fit together
    # and then thumbnail them down
    min_width = min([i.size[0] for i in image_list])
    min_height = min([i.size[1] for i in image_list])
    trim_list = []
    for x, i in enumerate(image_list):
        if i.size != (min_width, min_height):
            if verbose:
                print "Trimming %s" % (x+1)
            i = ImageOps.fit(i, (min_width, min_height))
        i.thumbnail((max_width, max_height), Image.ANTIALIAS)
        trim_list.append(i)
    # Create the GIF
    if verbose:
        print "Creating GIF at %s with duration of %s seconds each frame" % (
            gif_path, duration
        )
    trim_list.reverse()
    images2gif.writeGif(gif_path, trim_list, 
        duration=duration)

