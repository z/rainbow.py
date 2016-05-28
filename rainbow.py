# rainbow.py generates rainbow text!
# Tyler Mulligan
import configparser
import argparse
import json
import os
from colour import Color
from math import ceil


def main():

    args = parse_args()

    if args.string:
        phrase = args.string
    else:
        print('string required')
        raise SystemExit

    rainbow_text = generate_rainbow(phrase, args)

    print(rainbow_text)


def generate_rainbow(phrase, args):

    if not phrase:
        return False

    conf = parse_config('config.ini')

    opts = {}

    if args.colors:
        opts['color_count'] = int(args.colors)
    else:
        opts['color_count'] = int(conf['color_count'])

    if args.start_color:
        opts['start_color'] = args.start_color
    else:
        opts['start_color'] = conf['start_color']

    if args.end_color:
        opts['end_color'] = args.end_color
    else:
        opts['end_color'] = conf['end_color']

    if args.format:
        opts['output_format'] = args.format
    else:
        opts['output_format'] = conf['format']

    with open(conf['formats_file']) as f:
        opts['formats'] = json.loads(f.read())

    if opts['output_format'] in opts['formats']:
        template = opts['formats'][opts['output_format']]
    else:
        print('format not found! Are you sure it exists in ' + conf['formats_file'] + '?')
        raise SystemExit

    phrase_length = len(phrase)

    # chars per color
    cpc = ceil(phrase_length / opts['color_count'])

    color_start = Color(opts['start_color'])
    color_end = Color(opts['end_color'])
    rainbow = list(color_start.range_to(color_end, opts['color_count']))

    characters = list(phrase)
    characters.reverse()

    s = ''
    for color in rainbow:
        s += template['tag_open_before'] + color.hex + template['tag_open_after']

        i = 0
        while i < cpc and len(characters) > 0:
            next_char = characters.pop()
            s += next_char
            i += 1

        s += template['tag_close']

        if len(characters) < 1:
            break

    return s


def parse_config(config_file):

    if not os.path.isfile(config_file):
        print(config_file + ' not found, please create one.')
        raise SystemExit

    conf = configparser.ConfigParser()
    conf.read(config_file)

    return conf['default']


def parse_args():

    parser = argparse.ArgumentParser(description='A tool to generate rainbow text!')

    parser.add_argument('string', nargs='?', help='the phrase you want rainbowfied', type=str)
    parser.add_argument('--colors', '-c', nargs='?', help='number of colors to use in the range', type=str)
    parser.add_argument('--start_color', '-s', nargs='?', help='color to start on (default: red)', type=str)
    parser.add_argument('--end_color', '-e', nargs='?', help='color to end on (default: purple)', type=str)
    parser.add_argument('--format', '-f', nargs='?', help='output format from formats.json (default: html)', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    main()

