#!/usr/bin/env python3
"""Error recovery at each stage of scraping."""

#stand lib
from pathlib import Path

#custom
from constants import *
import scrapecategories as cat
import scrapeartists as art
import scrapesongs as song
import scrapelyrics as lyric

CATEGORY_ERRORS = CWD+"/categoryscrapingerrors.txt"
ARTIST_ERRORS   = CWD+"/artistscrapingerrors.txt"
SONG_ERRORS     = CWD+"/songscrapingerrors.txt"
LYRIC_ERRORS    = CWD+"/lyricscrapingerrors.txt"
ERROR_TEST      = CWD+"/songerrors_old.txt"
testerrors      = [ERROR_TEST]
errors          = [(CATEGORY_ERRORS, cat),
                   (ARTIST_ERRORS, art),
                   (SONG_ERRORS, song), 
                   (LYRIC_ERRORS, lyric)]

def errors_exist(file_):
    """Checks if any error exists in 'file_'. Returns Boolean."""
    return sum(1 for line in open(file_).readlines()) > 0

def recover(tuple_):
    """Recovers scraping errors from 'tuple_' pair.
        Uses the right scraping script for the right error.
        Returns None."""
    for line in open(tuple_[0]).readlines():
        tuple_[1].single_scrape(line)

#Main
print("--- ERROR RECOVERY, START---")
for pair in errors:
    print(pair[1].single_scrape)
print("--- ERROR RECOVERY, FINISHED ---")

