#!/usr/bin/env python3

import os
import sys

if __name__ == '__main__':
    section, foil, cap = None, None, 9999999
    if len(sys.argv) == 3:
        section, foil = sys.argv[2], sys.argv[1]
    elif len(sys.argv) == 4:
        section, foil, cap = sys.argv[2], sys.argv[1], int(sys.argv[3])
    else:  # len(sys.argv) != 3 or len(sys.argv) != 4:
        print('Please enter valid arguments.')
        sys.exit()

    with open(foil, 'r') as file:
        wordCount = 0
        active = False
        for line in file.readlines():
            line = line.strip()
            if active:
                real = not line.startswith('%') and line != '' and line != ' '
                if line == '}' or line == '} \\label{abstract}':
                    active = False
                elif real:
                    tempWords = []

                    for word in line.split(' '):
                        if not word.startswith('\\'):
                            tempWords += [word]

                    wordCount += len(tempWords)
                    #print(str(line) + ': ' + str(len(tempWords)))
            if not active and line.startswith('\\' + str(section) + '{'):
                active = True
        print('Word Count for: ' + str(section) + ':' +
              str(os.path.basename(foil)) + ' = ' + str(wordCount) + ' words')
        if wordCount > cap:
            print('Word Count Exceeded max length of :' + str(cap) + ' by ' +
                  str(wordCount - cap) + ' words')
            sys.exit(23)
