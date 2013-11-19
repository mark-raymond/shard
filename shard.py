#!/usr/bin/env python3

# shard.py
# Copyright 2013 Mark Raymond
# Released under the MIT license

import sys

if len(sys.argv) != 3:
  print('Usage: shard INPUT CHUNKS', file=sys.stderr)
  print('Shards INPUT line by line into CHUNKS files.', file=sys.stderr)
  exit(1)

filename = sys.argv[1]
chunks = sys.argv[2]

try:
  file = open(filename, 'rt')
except OSError:
  print('Could not open file "', filename, '"', sep='', file=sys.stderr)
  exit(1)

try:
  chunks = int(chunks)
except ValueError:
  print('"', chunks, '" is not a valid integer', sep='', file=sys.stderr)
  exit(1)

if (chunks < 2):
  print('Number of chunks must be at least 2', file=sys.stderr)
  exit(1)

format = filename + '.%0' + str(len(str(chunks - 1))) + 'd'
try:
  out = list(map(lambda i: open(format % i, 'wt'), range(chunks)))
except OSError:
  print('Could not open all output files', file=sys.stderr)
  exit(1)

i = 0
for line in file:
  out[i].write(line)
  i = (i + 1) % chunks
