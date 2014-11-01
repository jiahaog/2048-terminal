# -*- coding: UTF-8 -*-
#https://github.com/bfontaine/term2048

# Copyright © 2014 – Baptiste Fontaine

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




try:
    import termios
except ImportError:
    # Assume windows

    import msvcrt

    UP, DOWN, RIGHT, LEFT = 72, 80, 77, 75

    def getKey():
        while True:
            if msvcrt.kbhit():
                a = ord(msvcrt.getch())
                return a

else:
    # refs:
    # http://bytes.com/topic/python/answers/630206-check-keypress-linux-xterm
    # http://stackoverflow.com/a/2521032/735926
    import sys
    import tty

    __fd = sys.stdin.fileno()
    __old = termios.tcgetattr(__fd)

    # Arrow keys
    # they are preceded by 27 and 91, hence the double 'if' in getKey.
    UP, DOWN, RIGHT, LEFT = 65, 66, 67, 68

    # Vim keys
    K, J, L, H = 107, 106, 108, 104

    __key_aliases = {
        K: UP,
        J: DOWN,
        L: RIGHT,
        H: LEFT,
    }

    def __getKey():
        """Return a key pressed by the user"""
        try:
            tty.setcbreak(sys.stdin.fileno())
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            ch = sys.stdin.read(1)
            return ord(ch) if ch else None
        finally:
            termios.tcsetattr(__fd, termios.TCSADRAIN, __old)

    def getKey():
        """
        same as __getKey, but handle arrow keys
        """
        k = __getKey()
        if k == 27:
            k = __getKey()
            if k == 91:
                k = __getKey()

        return __key_aliases.get(k, k)

# legacy support
getArrowKey = getKey



__dirs = {
        UP:      'up',
        DOWN:    'down',
        LEFT:    'left',
        RIGHT:   'right',
    }


def readMove():
        """
        read and return a move to pass to a board
        """
        k = getKey()
        return __dirs.get(k)
