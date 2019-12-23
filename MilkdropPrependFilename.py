from __future__ import print_function

import argparse
import os
import sys

argparser = argparse.ArgumentParser(description='Prepend filenames to *.milk files')
argparser.add_argument('directory')
argparser.add_argument('-v', '--verbose', action='store_true')
args = argparser.parse_args()


def verbose(*msg):
    if args.verbose:
        print(*msg)


skipped = 0
processed = 0

for fname in os.listdir(args.directory):
    fpath = os.path.splitext(fname)
    if fpath[1] != '.milk':
        skipped += 1
        verbose('Skipping, non-milk:', fname)
        continue
    
    with open(os.path.join(args.directory, fname), 'rt+') as f:
        contents = f.read()
        comment = '//Original Filename - ' + fpath[0] + '\n'
        if contents.startswith(comment):
            verbose('Skipping, commented:', fname)
            skipped += 1
        else:
            verbose('Processing:', fname)
            f.seek(0)
            f.write(comment)
            f.write(contents)
            processed += 1

verbose('Finished: Processed:', processed, 'Skipped:', skipped)

