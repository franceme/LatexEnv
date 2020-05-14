#!/usr/bin/env python3

import os
import sys
import re

if (len(sys.argv) != 4):
    print('Usage: ./replace.py {file to move} {find} {replace}')
    sys.exit()

foil, find, replace = sys.argv[1], sys.argv[2], sys.argv[3]

if (not os.path.exists(foil)):
    print('File ' + str(foil) + ' does not exist')
    sys.exit(0)

#Moving the file from within main.tex
data = open(foil).read()
o = open(foil, "w")
o.write(re.sub(find, replace, data))
o.close()
