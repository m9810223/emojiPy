#!/usr/bin/env python3
import sys
from re import findall
from random import choice

from emojies import emojies


def main():
    if len(sys.argv) == 1:
        for line in sys.stdin:
            for e in findall(pattern=':.+?:', string=line):
                if e in emojies:
                    line = line.replace(e, emojies[e])
            try:
                print(line, end='')
            except Exception as e:
                print(e)
    elif sys.argv[1] in ('-l', '--list'):
        for k, v in emojies.items():
            print(v, k)
    elif sys.argv[1] in ('-r', '--random'):
        print(choice(list(emojies.values())))
    else:
        print('Faster 🚀 Python 🐍 emojify 🤗')
        print()
        print('Usage:  emojiPy [OPTIONS] [INPUT]')
        print()
        print('Options:')
        print('    -l, --list     List all emojies.')
        print('    -r, --random   Print a random emoji.')


if __name__ == '__main__':
    try:
        main()
        # https://docs.python.org/3/library/signal.html#note-on-sigpipe
        sys.stdout.flush()
    except BrokenPipeError:
        sys.stdout = None
