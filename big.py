class BigText:

    """A big text object that can be applied to a string"""

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
    }

    style = {
        '.': ' ',
        'o': '█',
    }

    def __init__(self):
        self.phrase = None
        self.generated = None

    def generate(self, phrase):

        # Get all rows from all letters in phrase onto 1 of 5 pixel_rows
        pixel_rows = [[], [], [], [], []]
        for letter in phrase.upper():
            if letter not in self.alphabet:
                print('Woah, no: ' + letter)
            else:
                for cell in range(5):
                    pixel_rows[cell] += self.alphabet[letter][cell]

        # wrap each pixel in a <td> and each row in a <tr>
        table_rows = [[], [], [], [], []]
        for i, row in enumerate(pixel_rows):
            table_rows[i] += '<tr>'
            for j, col in enumerate(row):
                table_rows[i] += '<td>' + self.style[col] + '</td>'
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


bt = BigText()
big = bt.generate(phrase='The quick brown fox jumped over the lazy dog.?!')
print(big)
