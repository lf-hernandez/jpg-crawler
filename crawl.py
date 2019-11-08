#!/usr/bin/python3

from sys import argv
from os import walk, path
from fnmatch import fnmatch
from shutil import move

rootdir = argv[1]

for root, dirs, files in walk(rootdir):
    for filename in files:
        if fnmatch(filename, '*.jpg'):
            print(f'moving {filename} to {rootdir}')
            absolutepath = path.join(root, filename)
            move(absolutepath, rootdir)
print('done.')
