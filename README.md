shard
=====

`shard.py` splits a file line by line into a number of files.

Usage: `shard.py input-file number-of-chunks`

This has a similar purpose to the Unix command `split`, but shards line by line instead of each output file having a continguous section of the original file. So, when splitting into two files, `split` will output two files, one containing the first half of the original file, and the other the second half. `shard.py` will output two files, one containing the even lines, the other the odd lines.
