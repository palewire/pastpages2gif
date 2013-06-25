<pre><code>                  _                                 ___          _  __ 
                 | |                               |__ \        (_)/ _|
  _ __   __ _ ___| |_ _ __   __ _  __ _  ___  ___     ) |   __ _ _| |_ 
 | '_ \ / _` / __| __| '_ \ / _` |/ _` |/ _ \/ __|   / /   / _` | |  _|
 | |_) | (_| \__ \ |_| |_) | (_| | (_| |  __/\__ \  / /_  | (_| | | |  
 | .__/ \__,_|___/\__| .__/ \__,_|\__, |\___||___/ |____|  \__, |_|_|  
 | |                 | |           __/ |                    __/ |      
 |_|                 |_|          |___/                    |___/       </code></pre>

Create an animated GIF from the [PastPages](http://www.pastpages.org) news homepage archive. An experiment with the [PastPages API](http://blog.pastpages.org/post/53734104165/say-hello-to-the-pastpages-api).

h3. Examples

```python
import pastpages2gif
from datetime import datetime

pastpages2gif.get_site(
    "./bbc.gif",
    "bbc",
    datetime(2012, 12, 31, 18, 0, 0),
    datetime(2013, 1, 1, 6, 0, 0),
    verbose=True
)
```

![BBC Fiscal Cliff](https://raw.github.com/pastpages/pastpages2gif/master/samples/bbc.gif)

```python
import pytz
import pastpages2gif
from datetime import datetime

pastpages2gif.get_site(
    "./boston-bombing.gif",
    "bostoncom",
    # Now with timezones
    datetime(2013, 4, 15, 11, 0, 0).replace(tzinfo=pytz.timezone("US/Eastern")),
    datetime(2013, 4, 17, 11, 0, 0).replace(tzinfo=pytz.timezone("US/Eastern")),
    verbose=True
)
```

![Boston Bombing](https://raw.github.com/pastpages/pastpages2gif/master/samples/boston-bombing.gif)


```python
import pytz
import pastpages2gif
from datetime import datetime

pastpages2gif.get_site(
    "./drudge-report.gif",
    "drudge-report",
    datetime(2012, 11, 6, 4, 0, 0).replace(tzinfo=pytz.timezone("US/Eastern")),
    datetime(2012, 11, 7, 4, 0, 0).replace(tzinfo=pytz.timezone("US/Eastern")),
    # Now with custom speed and size
    duration=1.0,
    max_width=900,
    max_height=2000,
    verbose=True
)
```

![Four more tears](https://raw.github.com/pastpages/pastpages2gif/master/samples/drudge-report.gif)

