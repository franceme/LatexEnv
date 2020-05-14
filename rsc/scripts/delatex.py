#!/usr/bin/env python3

##/usr/local/opt/python/bin/python2.7
# Change the line above according to your needs
#
# Copyright (c) 2014, Georgios Is. Detorakis (gdetor@gmail.com)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
'''
A very simple script, which clears all the latex-derivative files.
Example of usage:
    localhost@name$ ./latexdel destination-folder
'''
import os


def current_path():
    ''' Get the current path '''
    return os.getcwd()


def goto_directory(path):
    ''' Change directory moving to path'''
    return os.chdir(path)


def deletion(path):
    types = ('.log', '.aux', '.dvi', '.bbl', '.blg', '.glo', '.out', '.lot',
             '.lof', '.toc', '.not', '.bm', '.nav', '.snm', 'fls',
             'fdb_latexmk')

    for root, dirs, files in os.walk(path):
        for currentFile in files:
            if any(currentFile.lower().endswith(types) for ext in types):
                print("Deleting file: " + currentFile)
                os.remove(os.path.join(root, currentFile))


if __name__ == '__main__':
    if __name__ == '__main__':
        cp = current_path()
        # goto_directory(cp)
        deletion(cp)
