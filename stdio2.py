#!/usr/bin/env python

import sys
counter = 1
f = open('foo.txt', 'r')
print(type(sys.stdin) == type(f))


for i, line in enumerate(sys.stdin):
    print(f'{i} {line}')
 
