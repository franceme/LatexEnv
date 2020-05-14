#!/usr/bin/env python3

import os
import re
import sys

threshhold, command, reference, curLine = 15, re.compile(
    r'\\.*{.*}'), re.compile(r'\\ref{fig:.*}'), 0
parenthesis = re.compile(r'\(.*\)')

if (len(sys.argv) != 2):
    print('Usage: ./replace.py {file to move}')
    sys.exit()

foil = sys.argv[1]

if (not os.path.exists(foil)):
    print('File ' + str(foil) + ' does not exist')
    sys.exit(0)

#Reading the information in
data = []
max = 0
with open(foil, 'r') as file:
    pic = False
    for line in file.readlines():
        line = line.strip()
        if line.startswith('\\begin{figure}'):
            pic = True

        if not pic:

            if not line.startswith("%") and not line.startswith(
                    "\\") and not line.startswith("}") and line:
                temp = re.sub(command, "", line).replace("  ", " ")
                temp = re.sub(parenthesis, "", temp).replace("  ", " ")

                if len(temp.split()) >= threshhold:
                    print("Line " + str(curLine) + " {" + str(line) +
                          "} has " + str(len(temp.split()) - threshhold) +
                          " extra words")
                    max = max + 1
                    #sys.exit(222)

            line = re.sub(reference, "", line).replace("  ", " ")

            data += [line]

        if pic and line.startswith('\\end{figure}'):
            pic = False

        curLine = curLine + 1

print("Longest sentence is " + str(max) + " words")

with open(foil, 'w') as file:
    for line in data:
        file.write(line + '\n')
