from rainbow import Rainbow
from itertools import cycle
import argparse


def main():
    args = parse_args()

    if args.string:
        phrase = args.string
    else:
        print('string required')
        raise SystemExit

    bt = BigText()

    if not args.effect:
        html_output = bt.generate(phrase=phrase)
    elif args.effect == 'rainbow':
        html_output = bt.generate(phrase=phrase, effect='rainbow')

    print(html_output)


class BigText:

    """A big text object that can be applied to a string

    alphabet is a dictionary mapped to 5x5 characters
    phrase gets broken down by character to pushed onto 5 lists for the entire line of the phrase

    """

    alphabet = {
        'A': [
            '..o..',
            '.o.o.',
            'o...o',
            'ooooo',
            'o...o'
        ],
        'B': [
            'ooo..',
            'o..o.',
            'oooo.',
            'o...o',
            'oooo.'
        ],
        'C': [
            '.ooo.',
            'o...o',
            'o....',
            'o...o',
            '.ooo.',
        ],
        'D': [
            'ooo..',
            'o..o.',
            'o...o',
            'o...o',
            'oooo.',
        ],
        'E': [
            'ooooo',
            'o....',
            'ooo..',
            'o....',
            'ooooo',
        ],
        'F': [
            'ooooo',
            'o....',
            'ooo..',
            'o....',
            'o....',
        ],
        'G': [
            '.oooo',
            'o....',
            'o..oo',
            'o...o',
            '.oooo',
        ],
        'H': [
            'o...o',
            'o...o',
            'ooooo',
            'o...o',
            'o...o',
        ],
        'I': [
            'ooooo',
            '..o..',
            '..o..',
            '..o..',
            'ooooo',
        ],
        'J': [
            'ooooo',
            '...o.',
            '...o.',
            'o..o.',
            '.oo..',
        ],
        'K': [
            'o..o.',
            'o.o..',
            'ooo..',
            'o..o.',
            'o...o',
        ],
        'L': [
            'o....',
            'o....',
            'o....',
            'o....',
            'ooooo',
        ],
        'M': [
            'o...o',
            'oo.oo',
            'o.o.o',
            'o...o',
            'o...o',
        ],
        'N': [
            'o...o',
            'oo..o',
            'o.o.o',
            'o..oo',
            'o...o',
        ],
        'O': [
            '.ooo.',
            'o...o',
            'o...o',
            'o...o',
            '.ooo.',
        ],
        'P': [
            'oooo.',
            'o...o',
            'oooo.',
            'o....',
            'o....',
        ],
        'Q': [
            '.ooo.',
            'o...o',
            'o...o',
            'o.ooo',
            'ooo.o',
        ],
        'R': [
            'oooo.',
            'o...o',
            'oooo.',
            'o...o',
            'o...o',
        ],
        'S': [
            '.oooo',
            'o....',
            '.ooo.',
            '....o',
            'oooo.',
        ],
        'T': [
            'ooooo',
            '..o..',
            '..o..',
            '..o..',
            '..o..',
        ],
        'U': [
            'o...o',
            'o...o',
            'o...o',
            'o...o',
            '.ooo.',
        ],
        'V': [
            'o...o',
            'o...o',
            '.o.o.',
            '.o.o.',
            '..o..',
        ],
        'W': [
            'o...o',
            'o...o',
            'o.o.o',
            'o.o.o',
            '.o.o.',
        ],
        'X': [
            'o...o',
            'o...o',
            '.ooo.',
            'o...o',
            'o...o',
        ],
        'Y': [
            'o...o',
            'o...o',
            '.ooo.',
            '..o..',
            '..o..',
        ],
        'Z': [
            'ooooo',
            '...o.',
            '..o..',
            '.o...',
            'ooooo',
        ],
        ' ': [
            '.....',
            '.....',
            '.....',
            '.....',
            '.....'
        ],
        '.': [
            '.....',
            '.....',
            '.....',
            '.....',
            '.o...'
        ],
        ',': [
            '.....',
            '.....',
            '.....',
            '.o...',
            '.o...'
        ],
        '-': [
            '.....',
            '.....',
            '.ooo.',
            '.....',
            '.....'
        ],
        '_': [
            '.....',
            '.....',
            '.....',
            '.....',
            'ooooo'
        ],
        '?': [
            '.ooo.',
            'o...o',
            '..oo.',
            '.....',
            '..o..'
        ],
        '!': [
            '..o..',
            '..o..',
            '..o..',
            '.....',
            '..o..'
        ],
        '@': [
            '.oooo',
            'o....',
            'o.ooo',
            'o.o.o',
            '.ooo.'
        ],
        '#': [
            '.o.o.',
            'ooooo',
            '.o.o.',
            'ooooo',
            '.o.o.'
        ],
        '$': [
            '.ooo.',
            'o.o..',
            '.ooo.',
            '..o.o',
            '.ooo.',
        ],
        '%': [
            '...o.',
            '.o.o.',
            '..o..',
            '.o.o.',
            '.o...',
        ],
        '^': [
            '..o..',
            '.o.o.',
            'o...o',
            '.....',
            '.....',
        ],
        '&': [
            '.o...',
            'o.o..',
            '.ooo.',
            'o.o.o',
            '.ooo.',
        ],
        '*': [
            'o.o.o',
            '.ooo.',
            'ooooo',
            '.ooo.',
            'o.o.o',
        ],
        '(': [
            '.o...',
            'o....',
            'o....',
            'o....',
            '.o...',
        ],
        ')': [
            '...o.',
            '....o',
            '....o',
            '....o',
            '...o.',
        ],
    }

    style = {
        '.': ' ',
        'o': u'\u2588',  # █ block character
    }

    # TODO: Allow for alternative alphabet and style
    def __init__(self):
        self.phrase = None
        self.generated = None

    def generate(self, phrase, effect=None):

        # Get all rows from all letters in phrase onto 1 of 5 pixel_rows
        pixel_rows = [[], [], [], [], []]
        for index, letter in enumerate(phrase.upper()):

            if letter not in self.alphabet:
                print('character not found in mapping: ' + letter)
            else:
                for cell in range(5):
                    pixels = self.alphabet[letter][cell]
                    pixel_rows[cell] += pixels

        if effect == 'rainbow':
            rb = Rainbow(color_count=7)
            rb.get_rainbow('The quick brown fox jumped over the lazy dog.?!')
            colors = cycle(rb)
            current_color = str(next(colors))

        # wrap each pixel in a <td> and each row in a <tr>
        table_rows = [[], [], [], [], []]
        for i, row in enumerate(pixel_rows):

            table_rows[i] += '<tr>'

            for j, col in enumerate(row):

                pixel = self.style[col]

                if effect == 'rainbow':
                    current_color = str(next(colors))
                    if pixel == self.style['o']:
                        pixel = '<span style="color:' + current_color + '">' + pixel + '</span>'

                table_rows[i] += '<td>' + pixel + '</td>'

                if j % 5 == 4:  # put a space between each character
                    table_rows[i] += '<td> </td>'

            table_rows[i] += '</tr>'

        table_output = '<table>'
        for row in range(5):
            table_output += ''.join(table_rows[row])
        table_output += '</table>'

        self.phrase = phrase
        self.generated = table_output

        return table_output


def parse_args():

    parser = argparse.ArgumentParser(description='A tool to generate big text!')

    parser.add_argument('string', nargs='?', help='the phrase you want big', type=str)
    parser.add_argument('--effect', '-f', nargs='?', help='output effect (default: none)', type=str)

    return parser.parse_args()

if __name__ == '__main__':
    main()
