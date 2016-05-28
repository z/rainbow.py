# rainbow.py

Generate rainbow text with rainbow.py!

### Installation

```
virtualenv -p /usr/bin/python3 venv
ln -s venv/bin/activate
source activate
pip install -r requirements.txt
```

### Configuration

```
cp example.config.ini config.ini
cp example.formats.json formats.json
```

Default contents look similar to below:

```
[default]

color_count  = 12
start_color  = red
end_color    = purple
format       = html
formats_file = formats.json
```

Formats are defined in `formats.json` and look similar to below:

```
{
    "html": {
        "tag_open_before": "<span style=\"color:",
        "tag_open_after": "\">",
        "tag_close": "</span>"
    },
    "html_single": {
        "tag_open_before": "<span style='color:",
        "tag_open_after": "'>",
        "tag_close": "</span>"
    }
}
```

### Usage

```
usage: rainbow.py [-h] [--colors [COLORS]] [--start_color [START_COLOR]]
                [--end_color [END_COLOR]] [--format [FORMAT]]
                [string]

A tool to generate rainbow text!

positional arguments:
  string                the phrase you want rainbowfied

optional arguments:
  -h, --help            show this help message and exit
  --colors [COLORS], -c [COLORS]
                        number of colors to use in the range
  --start_color [START_COLOR], -s [START_COLOR]
                        color to start on (default: red)
  --end_color [END_COLOR], -e [END_COLOR]
                        color to end on (default: purple)
  --format [FORMAT], -f [FORMAT]
                        output format from formats.json (default: html)
```

#### tl;dr

```
python rainbow.py "testing my custom rainbow"
```
