import sys
import unittest
from contextlib import contextmanager

import antsy


def print_demo():
    print('All tests finished, printing manual verification page...\n')
    # Some manual formatting tests
    print(antsy.decorate(
        'Some text and then (bold bold text and then (fg/red bold red text) now bold) and normal'))
    print(antsy.decorate(
        '(b bold) (d dim) (i italic) (u underline) (b,fg/red DANGER) (bg/green,i,u,fg/yellow CRAZY)'))
    print(antsy.decorate(
        'Different delimiters here (because this text has [fg/red parentheses] in it)', start='[', end=']'))
    # The table
    print(antsy.decorate(''.join(
        ['        '] + ['(fg/{} {})'.format(c, c.ljust(8)) for c in antsy.COLORS])))
    for bgc in antsy.COLORS:
        sys.stdout.write(antsy.decorate(
            '(bg/{} {}) '.format(bgc, bgc.ljust(7))))
        for fgc in antsy.COLORS:
            sys.stdout.write(antsy.decorate(
                '(bg/{}  (fg/{} (d X) X (b X)) ) '.format(bgc, fgc)))
        sys.stdout.write('\n')
    # Some room for the table to breathe
    print('')


@contextmanager
def support(on):
    temp = antsy.SUPPORTS_COLOR
    antsy.SUPPORTS_COLOR = on
    yield
    antsy.SUPPORTS_COLOR = temp


class TestAntsy(unittest.TestCase):

    def run_spec(self, d, start='(', end=')'):
        self.assertEqual(antsy.decorate(
            d['actual'], start=start, end=end), d['on'])
        with support(False):
            self.assertEqual(antsy.decorate(
                d['actual'], start=start, end=end), d['off'])

    def test_codes(self):
        self.run_spec({
            'actual': '(normal a)(bold b)(dim c)(italic d)(underline e)(fg/red f)(bg/red g)',
            'on': 'a\x1b[1mb\x1b[22m\x1b[2mc\x1b[22m\x1b[3md\x1b[23m\x1b[4me\x1b[24m\x1b[31mf\x1b[39m\x1b[41mg\x1b[49m',
            'off': 'abcdefg'
        })

    def test_abbreviations(self):
        self.run_spec({
            'actual': '(n a)(b b)(d c)(i d)(u e)',
            'on': 'a\x1b[1mb\x1b[22m\x1b[2mc\x1b[22m\x1b[3md\x1b[23m\x1b[4me\x1b[24m',
            'off': 'abcde'
        })

    def test_nested(self):
        self.run_spec({
            'actual': 'a (b b (d c (i d (u e) f) g) h) i',
            'on': 'a \x1b[1mb \x1b[2mc \x1b[3md \x1b[4me\x1b[24m f\x1b[23m g\x1b[22m h\x1b[22m i',
            'off': 'a b c d e f g h i'
        })

    def test_multiple(self):
        self.run_spec({
            'actual': '(b,i,u,fg/magenta,bg/yellow This is awesome!)',
            'on': '\x1b[43m\x1b[35m\x1b[4m\x1b[3m\x1b[1mThis is awesome!\x1b[22m\x1b[23m\x1b[24m\x1b[39m\x1b[49m',
            'off': 'This is awesome!'
        })

    def test_custom_delimiters(self):
        self.run_spec({
            'actual': '[b Look at the blue man: [fg/blue (:-O)->--<]]',
            'on': '\x1b[1mLook at the blue man: \x1b[34m(:-O)->--<\x1b[39m\x1b[22m',
            'off': 'Look at the blue man: (:-O)->--<'
        }, start='[', end=']')


class TestErrors(unittest.TestCase):
    '''Errors a user could make formatting strings'''

    def test_delimiters_same(self):
        with self.assertRaises(SyntaxError):
            antsy.decorate('This will fail', start='!', end='!')

    def test_undefined_code(self):
        with self.assertRaises(SyntaxError):
            antsy.decorate('Well (this is not going to work)')


class TestCompatibility(unittest.TestCase):
    '''antsy should work on non-ANSI capable terminals'''

    def test_not_supports_color(self):
        with support(False):
            actual = antsy.decorate(
                'This (bold should) (i go through (bg/green unchanged))')
            self.assertEqual(actual, 'This should go through unchanged')


if __name__ == '__main__':
    unittest.main(exit=False)
    print_demo()
