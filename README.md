# LatexEnv

## What is this?

This is a subset python scripts used to make my life writing tex files simple.
When you compile a project on Overleaf you can use a simple spell check but nothing else.
You are not able to add custom scripts to help manipulate or check.
Listed below are the benefits of using each of the scripts:

* delatex
    * Used to remove various compilation files from a latex build
* flatten
    * "flattens" or puts all of the sections into one latex file
* removePic
    * Removes the pictures from the main file
* replace
    * Replaces a word (string) with another word (string)
* singlewordcounter
    * Counts the occurences of a word within a tex file.
* texcheck
    * Ensures bib entries are cited and sources.
* wordcount
    * Counts the number of words from a section.

I have hooked these into a Makefile, to make it easier to use.
Why a Makefile?
Simple, its likely more available than python.

## Sources
* [delatex.py](./rsc/scripts/delatex.py) - [gdetor/LatexTools](https://github.com/gdetor/LatexTools)
    * Under BSD 2-Clause "Simplified" License, Modified from its original form
* [flatten.py](./rsc/scripts/flatten.py) - [lukeolson/clean-latex-to-arxiv](https://github.com/lukeolson/clean-latex-to-arxiv)
    * Under MIT License, Modified from its original form
* [texcheck.py](./rsc/scripts/texcheck.py) - [awstuff/texcheck](https://github.com/awstuff/texcheck)
    * Under MIT License, Modified from its original form