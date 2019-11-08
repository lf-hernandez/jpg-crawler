#!/usr/bin/python3

import sys
import os
import fnmatch
from shutil import move

rootDir = sys.argv[1]

for root, dirs, files in os.walk(rootDir):
    for filename in files:
        if fnmatch.fnmatch(filename, '*.jpg'):
            print(f'moving {filename} to {rootDir}')
            absolutePath = os.path.join(root, filename)
            move(absolutePath, rootDir)
print('done.')