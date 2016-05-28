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

    rb = Rainbow(args.colors, args.start_color, args.end_color, args.format)
    rainbow_text = rb.generate(phrase)

    print(rainbow_text)


class Rainbow(object):
    """A rainbow object that can be applied to a string"""

    def __init__(self, color_count, start_color, end_color, output_format):

        conf = parse_config('config.ini')

        self.color_count = int(conf['color_count'])
        self.start_color = conf['start_color']
        self.end_color = conf['end_color']
        self.output_format = conf['format']

        if color_count:
            self.color_count = int(color_count)

        if start_color:
            self.start_color = start_color

        if end_color:
            self.end_color = end_color

        if output_format:
            self.output_format = output_format

        with open(conf['formats_file']) as f:
            self.formats = json.loads(f.read())

        if self.output_format in self.formats:
            self.template = self.formats[self.output_format]
        else:
            raise RuntimeError('format not found! Are you sure it exists in ' + conf['formats_file'] + '?')


    def generate(self, phrase):
    
        phrase_length = len(phrase)

        # chars per color
        cpc = ceil(phrase_length / self.color_count)

        color_start = Color(self.start_color)
        color_end = Color(self.end_color)
        rainbow = list(color_start.range_to(color_end, self.color_count))

        characters = list(phrase)
        characters.reverse()

        s = ''
        for color in rainbow:
            s += self.template['tag_open_before'] + color.hex + self.template['tag_open_after']

            i = 0
            while i < cpc and len(characters) > 0:
                next_char = characters.pop()
                s += next_char
                i += 1

            s += self.template['tag_close']

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

