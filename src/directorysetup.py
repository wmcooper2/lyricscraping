#!/usr/bin/env python3
"""This module sets up the directory structure for webscraping.

    This program creates files and directories in '/Volumes/YUUSHI/`

"""
#stand lib
from pathlib import Path

#custom
from constants import *

dirs = [
    CATEGORY_DIR,
    ARTIST_DIR,
    SONG_DIR,
#    LYRIC_DIR
]

files = [
    CATEGORY_ERRORS,
    CATEGORY_STATS,
    ARTIST_ERRORS,
    ARTIST_STATS,
    SONG_ERRORS,
    SONG_STATS,
#    LYRIC_ERRORS,
#    LYRIC_STATS
]

def check(list_):
    """Checks that all paths in 'list_' exist.
        Returns Boolean."""
    return all([Path(x).exists() for x in list_])

def makedirs(list_):
    """Makes directories in 'list_' if they don't exist.
        Returns None."""
    for path in list_:
        if Path(path).exists():
            pass
        else:
            Path(path).mkdir()
            print("CREATED:\t", path)

def makefiles(list_):
    """Makes files in 'list_' if they don't exist.
        Returns None."""
    for path in list_:
        if Path(path).exists():
            pass
        else:
            Path(path).mkdir()
            print("CREATED:\t", path)

#Main
if __name__ == "__main__":
    print("--- DIRECTORY/FILE CHECK, START---")
    if check(dirs):
        print("Directories are in place.")
    else:
        makedirs(dirs)
        print("Directories are in place.")
    if check(files):
        print("Files are in place.")
    else:
        makefiles(files)
        print("Files are in place.")
    print("--- DIRECTORY/FILE CHECK, FINISH---")






