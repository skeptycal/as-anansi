#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
''' anansi.py - Tricky and fun ansi text utilities for python programs.
        import anansi or use with the following CLI syntax:

    Usage:
        anansi TEXT [-z]
        anansi FILE(s) [-Rz] [-q | -v ] [--pattern PATTERN]
        anansi TEMPLATE [-Rz] [-q | -v] [--pattern PATTERN]
        anansi [--help | --version]

    Options:
        FILE(s)                 Search pattern to match
        -q, --quiet             suppress most error messages  [default: True]
        -R --recursive          Perform search recursively    [default: False]
        -v --verbose            Display detailed progress     [default: False]
        -z, --zero              end each output line with NUL [default: False]

        -P PATTERN --pattern PATTERN    Pattern to highlight  [default: None]

        --version               Show version.
        --debug                 Show debug info and test results.
        -h --help               Show this screen.

    Exit status:

        0 if all file names were printed without issue.
        1 otherwise.

    Based on ANSI standard ECMA-48:
    http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
    '''

'''               Anansi, A Bit of Lore

    # - named after Anansi, the trickster, of West African and Caribbean
    #   folklore. Before Anansi, there were no stories in the world. What
    #   a terrible and ignorant place that must have been!

    # It was Anansi who convinced Nyame, The Sky-God, to share his stories
    #   with the world, but only after capturing the Python, the Hornets,
    #   the Leopard, and the Fairy.
    '''

""" # ########################################## TODO: Ideas and additions:

    1. integrate into <str> class so it works well with others ...
        e.g. output = some_string.capitaize.BLUE.strip

    2. Random changing letter colors in words
        (iterate over letters, interleve random formatting)

    3. Patterned changing letter colors in words
        (zip formatting with letters, join)

    4. Slice formatting options for sentences similar to sometext.format(x, y)
        e.g. some_string.format("1:3, 3, 4:6, 6:", [BLUE, RED, Color248,
        YELLOW]) (break string into slices, prepend formatting, join)

    5. Add common color formats and interfaces
        css parsing, js library, 16bit color, 32bit color, etc.

     """
# noqa: E731, E123, F401
# flake8: noqa
# - ------------------------ Imports
if True:  # stupid VSCode formatting thing
    from enum import Enum, auto
    import os
    import time
    import re
    import sys
    from typing import Any, Iterator, List
    if True:
        try:
            import ujson as json  # use faster version if available
        except ImportError:
            import json  # type: ignore

# ------------------------------- Utilities

# ------------------------------- GENERAL CONSTANTS


class GIX_STC:  # @v --> Structural Thinking Comments
    # @context --> GIX STC DEKO Comments VSCode Addon
    # @d --> https://github.com/GuillaumeIsabelleX/gixdeko-comments
    # @d --> https://marketplace.visualstudio.com/items?itemName=GuillaumeIsabelle.gixdeko-comments
    # @d --> https://www.youtube.com/watch?v=MnzKC24QvBI&list=PL0TcUolAT49gQ5tdyBvczwm3s-k3v02g4

    ##########################################################################
    # @vision -->
    # @action -->
    # @obs -->
    # @cr -->
    # // Strikethrough
    # @status -->
    # @question -->
    # @issue -->
    # @context -->
    # @concept -->
    # @data -->
    # @bug -->
    # @test -->
    # @insight -->
    # @due -->
    # @mastery -->
    # _	--> Separate code with visual // _ Different colored      ...
    # -	--> Separate code with visual // -----Nice separator----- ...
    # ###... Contrasted visual separator

    # @v <s> standard
    # @v <t> t
    # @v <u> u
    # @v <p> python
    # @v <i> i
    # @v <d> d
    pass


""" # ------------------------------- Color formatting
    #p1 {background-color: #ff0000;}                /* red in HEX format */
    #p2 {background-color: hsl(120, 100%, 50%);}    /* green in HSL format */
    #p3 {background-color: rgba(0, 4, 255, 0.733);} /* blue with alpha channel in RGBA format */
    """

# ------------------------------- Ansi Class


class Ansi(Enum):
    """ ANSI color magic 🦄  """
    # - some favorites
    MAIN: str = "\x1B[38;5;229m"
    WARN: str = "\x1B[38;5;203m"
    BLUE: str = "\x1B[38;5;38m"
    GO: str = "\x1B[38;5;28m"
    CHERRY: str = "\x1B[38;5;124m"
    CANARY: str = "\x1B[38;5;226m"
    ATTN: str = "\x1B[38;5;178m"
    RAIN: str = "\x1B[38;5;93m"
    WHITE: str = "\x1B[37m"
    RESET: str = "\x1B[0m"  # - reset ansi effects
    RESTORE: str = "\x1B[0m"  # - alias of RESET

    # - Encode ANSI effect set
    BOLD: str = "\x1B[1m"
    FAINT: str = "\x1B[2m"
    ITALIC: str = "\x1B[3m"
    IT: str = "\x1B[3m"
    UNDERLINE: str = "\x1B[4m"
    UL: str = "\x1B[4m"
    BLINK: str = "\x1B[5m"
    REVERSE: str = "\x1B[7m"
    CONCEAL: str = "\x1B[8m"
    STRIKE: str = "\x1B[9m"
    FRAME: str = "\x1B[51m"
    CIRCLE: str = "\x1B[52m"
    OVERLINE: str = "\x1B[53m"

    # - Encode ANSI 4-bit foreground color set
    Black: str = "\x1B[30m"
    Red: str = "\x1B[31m"
    Green: str = "\x1B[32m"
    Yellow: str = "\x1B[33m"
    Blue: str = "\x1B[34m"
    Magenta: str = "\x1B[35m"
    Cyan: str = "\x1B[36m"
    White: str = "\x1B[37m"

    # - Encode extended ANSI 4-bit foreground color set
    BrightBlack: str = "\x1B[30;1m"
    BrightRed: str = "\x1B[31;1m"
    BrightGreen: str = "\x1B[32;1m"
    BrightYellow: str = "\x1B[33;1m"
    BrightBlue: str = "\x1B[34;1m"
    BrightMagenta: str = "\x1B[35;1m"
    BrightCyan: str = "\x1B[36;1m"
    BrightWhite: str = "\x1B[37;1m"

    # - Encode ANSI 4-bit background color set
    BBlack: str = "\x1B[40m"
    BRed: str = "\x1B[41m"
    BGreen: str = "\x1B[42m"
    BYellow: str = "\x1B[43m"
    BBlue: str = "\x1B[44m"
    BMagenta: str = "\x1B[45m"
    BCyan: str = "\x1B[46m"
    BWhite: str = "\x1B[47m"

    # - Encode extended ANSI 4-bit background color set
    BBrightBlack: str = "\x1B[40;1m"
    BBrightRed: str = "\x1B[41;1m"
    BBrightGreen: str = "\x1B[42;1m"
    BBrightYellow: str = "\x1B[43;1m"
    BBrightBlue: str = "\x1B[44;1m"
    BBrightMagenta: str = "\x1B[45;1m"
    BBrightCyan: str = "\x1B[46;1m"
    BBrightWhite: str = "\x1B[47;1m"

    # ------------------------ general constants
    NL:     str = os.linesep    # -or- chr(10)  # newline character
    NUL:    str = chr(0)        # - NUL character
    BAK:    str = chr(8)        # - Backspace character
    TAB:    str = chr(9)        # - Horizontal Tab character
    LF: str = chr(10)           # - Linefeed

    ESC: str = '\x1B'           # - Escape

    # ------------------------ ansi code constants
    ANSI_SEP: str = ';'
    CSI: str = ESC + '['  # - ANSI ECMA-48 Control Sequence Introducer
    CSI_8bit: str = CSI + '38;5;'  # - prefix for 256 color codes
    SUFFIX: str = 'm'  # - suffix for ansi codes
    SUPPORTS_COLOR: bool = self.ssupports_color()

    # ------------------------ ansi format strings
    # - {n} - format string for basic 4 bit ansi escape codess
    fmt_CSI: str = CSI + '{}m'
    # - {3,4}{0-255} - format string for 256 color codes
    # - 3 is foreground; 4 is background
    fmt_CSI_8bit: str = CSI_8bit + '{}{}m'

    # ------------------------ default ANSI values
    DEFAULT_FG_CODE:        int = 229
    DEFAULT_BG_CODE:        int = 0
    DEFAULT_EFFECT_CODE:    int = 0
    DEFAULT_FG:             str = MAIN
    DEFAULT_BG:             str = BBlack

    def __init__(self):
        super().__init__()
        self._add_8bit()

    def add_dynamic_method(self, name, value):
        """ Add dynamic method to class. """

        def key_method(self, value=value):
            """ Dynamic method that returns <value>. """
            return value
        setattr(self.__class__, name, value)

    def _add_8bit():
        """ Create dynamic color methods for each ANSI 256 color codes. """
        for i in range(255):
            name = f"color{i}" if i < 233 else f"grey{i}"
            self.add_dynamic_method(name, self.fg(i))
            self.add_dynamic_method('bg' + name, self.bg(i))

    def is_a_tty():
        ''' True if tty and stdout availale.

            (from https://github.com/willyg302) '''
        return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

    def supports_color():
        ''' True if the terminal supports color.

            Sort of from Django.
            (from https://github.com/willyg302)'''
        if not self.is_a_tty():
            return False
        platform = sys.platform
        if platform == 'Pocket PC':
            return False
        if platform == 'win32' and 'ANSICON' not in os.environ:
            return False
        return True


class AnsiUtilities(object):
    """ ANSI color magic 🦄  """

    def __init__(self):
        self.load_colors()
        super().__init__()

    def encode_color_str(self,
                         fg: int = Ansi().DEFAULT_FG_CODE,
                         bg: int = Ansi().DEFAULT_BG_CODE
                         ):
        print(self.fg(fg), self.bg(bg))

    def encode_color_tuple(self,
                           fg: int = Ansi().DEFAULT_FG_CODE,
                           bg: int = Ansi().DEFAULT_BG_CODE,
                           ef: int = Ansi().DEFAULT_EFFECT_CODE
                           ):

        print(self.encode(ef), self.bg(bg), self.fg(fg))

    def encode(self, ef: int = 0):
        print(Ansi().fmt_CSI.format(ef))

    def fg(self, color: int = 15) -> str:
        """ Encode ANSI 8-bit foreground color (default: 15)

                foreground encoding - `ESC[38;5;3{color}m`

            color -
            - 0-7:     standard colors(e.g. 4-bit ESC[30–37 m)
            - 8-15:    high intensity colors(e.g. 4-bit ESC[90–97 m)
            - 16-231:  6×6×6 cube(216 colors) 16 + 36×r + 6×g + b(0 ≤ r, g, b ≤ 5)
            - 232-255: grayscale from black to white in 24 steps
            """
        return f"\x1b[38;5;3{color}m"

    def bg(self, color: int = 0) -> str:
        """ Encode ANSI 8-bit background color (default: 0)

                background encoding - `ESC[48;5;4{color}m`

            color -
            - 0-7:     standard colors(e.g. 4-bit ESC[30–37 m)
            - 8-15:    high intensity colors(e.g. 4-bit ESC[90–97 m)
            - 16-231:  6×6×6 cube(216 colors) 16 + 36×r + 6×g + b(0 ≤ r, g, b ≤ 5)
            - 232-255: grayscale from black to white in 24 steps
            """
        return f"\x1b[38;5;4{color}m"

    def load_colors(self):
        for _ in range(232):
            name = f'color{_}' if _ < 233 else f'grey{_}'
            value = self.fmt_CSI_8bit.format('3', _)
            self.add_dynamic_method(name, value)

            name = f'bgcolor{_}' if _ < 233 else f'bggrey{_}'
            value = self.fmt_CSI_8bit.format('4', _)
            self.add_dynamic_method(name, value)

# ------------------------ ANSI cursor controls

    def loading(self, delay: float = 0.1, message: str = 'Loading ...', percent: bool = True):
        """ ### Terminal progress Indicator

            # Usage:

                loading(delay: float = 0.1, message: str = 'Loading ...', percent: bool = True )


                delay - delay between ticks
                message - feedback shown during countdown (default: 'Loading...')
                percent - display the '%' symbol

            """
        sp: str = '%'
        if not percent:
            sp = ''
        print(message)
        for i in range(0, 100):
            time.sleep(delay)
            sys.stdout.write("\x1B[1000D" + str(i + 1) + sp)
            sys.stdout.flush()
        print()

    def move_to(self, L: int, C: int):
        """ Position the Cursor:

                <ESC>[<L>;<C>H
                    Or
                <ESC>[<L>;<C>f

            puts the cursor at line L and column C.
            """
        print(f"\x1B[{L};{C}H")

    def up(self, n: int = 1):
        """ Move the cursor up N lines:

                <ESC>033[<N>A
            """
        print(f"\x1B[{n}A")

    def down(self, n: int = 1):
        """ Move the cursor down N lines:

                <ESC>033[<N>A
            """
        print(f"\x1B[{n}B")

    def left(self, n: int = 1):
        """ Move the cursor forward N columns:

                <ESC>033[<N>A
            """
        print(f"\x1B[{n}C")

    def right(self, n: int = 1):
        """ Move the cursor backward N columns:

                <ESC>033[<N>A
            """
        print(f"\x1B[{n}D")

    def clear(self):
        """ Clear the screen, move to (0,0):

                <ESC>033[2J
            """
        print(f"\x1B2J")

    def eof(self):
        """ Erase to end of line:

                <ESC>033[K
            """
        print(f"\x1BK")

    def save_cursor(self):
        """ Save cursor position:

                <ESC>033[s
            """
        print(f"\x1Bs")

    def restore_cursor(self):
        """ Restore cursor position:

                <ESC>033[u
            """
        print(f"\x1Bu")


def dbprint(*args, db: bool = False, color: str = "\x1B[38;5;178m", sep='', end=Ansi.NL, file=sys.stderr, flush=False):
    ''' Prints debug messages if db flag is True.

        - db - boolean flag for debug state
        - color - keyword argument for print color. (default: Ansi.WARN)

        Example:
        ```py
        if args[0] == '--version':
            dbprint(f"{Ansi.MAIN}anansi.py{Ansi.RESET} version {__version__}.",
                    db = SET_DEBUG, end=f"<--debug{os.linesep}")
        ```

        '''
    if db:
        print(color, *args, Ansi.RESET, sep=sep,
              end=f"<--debug{Ansi().NL}", file=file, flush=flush)


def main(args):
    """ main loop - test ansi cli functions """
    a = Ansi_Utilities()
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    # dbprint(f"{args=}")
    dbprint(a.move_to(2, 3))
    dbprint(f"{supports_color()=}")
    if len(args) > 0:
        if args[0] == '--debug':
            SET_DEBUG = True
        if args[0] == '--version':
            print(f"{Ansi.MAIN}ansi.py{Ansi.RESET} version {__version__}.")
            # sys.exit(0)
        if args[0] == '--help':
            print(__doc__)
            # sys.exit(0)
        for arg in args:
            arg.upper()
            # print(Ansi(f"{arg}"))
    # dbp   rint(
        # f"{Ansi.BLUE}This is blue{Ansi.RESET} ... and {Ansi.CHERRY}this is red.{Ansi.RESET}")


if __name__ == "__main__":
    """ cli version """
    #! use test_args to override sys.argv for testing
    test_args: List[str] = []
    main(test_args)


# Ref
# Issue with Windows registry setting:
#   https://stackoverflow.com/a/57154895
#   File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/enum.py", line 221, in __new__
