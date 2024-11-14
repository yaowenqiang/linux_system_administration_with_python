#!/usr/bin/env python

import sys
counter = 1
f = open('foo.txt', 'r')
print(type(sys.stdin) == type(f))

while True:
    line = sys.stdin.readline()
    if not line:
        break
    print(f"{counter}: {line}")
    counter += 1


