#!/usr/bin/env python3

import os
import sys

if __name__ == '__main__':
    string, foil = None, None
    if len(sys.argv) == 3:
        string, foil = sys.argv[2], sys.argv[1]
    else:  # len(sys.argv) != 3 or len(sys.argv) != 4:
        print('Please enter valid arguments.')
        sys.exit()

    with open(foil, 'r') as file:
        wordCount = 0
        for line in file.readlines():
            line = line.strip()
            real = not line.startswith('%') and line != '' and line != ' '
            if real:
                wordCount += line.split().count(str(string))
                wordCount += line.split().count(str(string.capitalize()))

        print('Word Count for: ' + str(string) + ': in ' +
              str(os.path.basename(foil)) + ' = ' + str(wordCount) + ' times')
        if wordCount > 0:
            print('Too many')
            sys.exit(22)
