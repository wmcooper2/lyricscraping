#!/usr/bin/env python3
"""Container module for constants."""

from pathlib import Path

CWD             = str(Path.cwd())
ROOT            = "/"+"/".join(Path.cwd().parts[1:-1])
HOME_PAGE       = "https://www.lyrics.com"
PUNCTUATION     = "/"
BACKUPDIR       = CWD+"/BACKUP"

CATEGORY_DIR    = CWD+"/allcategories"
CATEGORY_ERRORS = CWD+"/allcategories/categoryscrapingerrors.txt"
CATEGORY_FILE   = CWD+"/allcategories/allcategories.txt"
CATEGORY_STATS  = CWD+"/allcategories/categorystats.txt"

ARTIST_DIR      = CWD+"/allartists"
ARTIST_FILE     = CWD+"/allartists/longlistofartists.txt"
ARTIST_ERRORS   = CWD+"/allartists/artistscrapingerrors.txt"
ARTIST_STATS    = CWD+"/allartists/artiststats.txt"

SONG_DIR        = CWD+"/allsongs/"
SONG_ERRORS     = CWD+"/allsongs/songscrapingerrors.txt"
SONG_FILE       = CWD+"/lyricscrapingerrors.txt"
SONG_STATS      = CWD+"/allsongs/songstats.txt"
SONG_SET_FILE   = CWD+"/allsongs/songset.txt"

# be careful with this until done scraping
LYRIC_DIR       = CWD+"/alllyrics"
LYRIC_ERRORS    = CWD+"/lyricscrapingerrors.txt"
#LYRIC_FILE      = CWD+"/longlistoflyrics.txt"
#LYRIC_STATS     = CWD+"/lyricstats.txt"

# command scripts
MOVE_SCRIPT      = ROOT+"/movetocategories"
BACKUP_SCRIPT    = ROOT+"/backup"
DIR_SCRIPT       = ROOT+"/dirsetup"
SCRAPE_SCRIPT    = ROOT+"/scrape"

# custom modules
SCRAPE_CATEGORIES= CWD+"/scrapecategories.py"
SCRAPE_ARTISTS   = CWD+"/scrapeartists.py"
SCRAPE_SONGS     = CWD+"/scrapesongs.py"
SCRAPE_LYRICS    = CWD+"/scrapelyrics.py"

# GUI
S_WIDTH         = 10
M_WIDTH         = 20
L_WIDTH         = 30
XL_WIDTH        = 40


