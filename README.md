# rainbow.py

Generate rainbow text with rainbow.py!

### Installation

```
virtualenv -p /usr/bin/python3 venv
ln -s venv/bin/activate
source activate
pip install -r requirements.txt
cp example.config.ini config.ini
cp example.formats.json formats.json
```

### Usage

Make sure you're in the venv with `source activate`.

##### A basic rainbow

```sh
python rainbow.py "testing my custom rainbow"
```

##### A rainbow with different start and end colors

```sh
python rainbow.py "rainbow with a different start and end color" --start_color pink --end_color green
```

##### A rainbow with only 3 colors

```sh
python rainbow.py "rainbow that only uses three colors" -c 3
```

##### All Options

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

### Configuration

Default contents for `config.ini` look similar to below:

```ini
[default]

color_count  = 12
start_color  = red
end_color    = purple
format       = html
formats_file = formats.json
```

Formats are defined in `formats.json` and look similar to below:

```json
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
