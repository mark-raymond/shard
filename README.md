# shard

## Description

`shard` splits a file line by line into a number of files.

This has a similar purpose to the Unix command `split`, but shards line by line instead of each output file having a continguous section of the original file. So, when splitting into two files, `split` will output two files, one containing the first half of the original file, and the other the second half. `shard` will output two files, one containing the odd lines, the other the even lines.

## Usage

`shard input-file number-of-chunks`

For example, `shard long-file.txt 3` will produce three files called `long-file.txt.0`, `long-file.txt.1` and `long-file.txt.2`, each having every third line from `long-file.txt`.

## Installation

`sudo install shard.py /usr/local/bin/shard`
