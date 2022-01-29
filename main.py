#!/usr/bin/env python3
from sys import stdin, stdout, argv
from re import findall

from emojies import emojies

if len(argv) == 1:
    for line in stdin:
        for e in findall(pattern=':.+?:', string=line):
            if e in emojies:
                line = line.replace(e, emojies[e])
        stdout.write(line)
elif argv[1] in ('-l', '--list'):
    for k, v in emojies.items():
        print(v, k)
else:
    print('Faster 🚀 Python 🐍 emojify 🤗')
    print()
    print('Usage:  emojiPy [OPTIONS] [INPUT]')
    print()
    print('Options:')
    print('    -l, --list     List all emojies.')
