#!/usr/bin/env python3
"""Test module for the webscraping project"""

#stand lib
from pathlib import Path
import requests

#custom
from constants import *

# directory existence 
def test_dirs():
    assert Path(CATEGORY_DIR).exists() is True
    assert Path(ARTIST_DIR).exists() is True
    assert Path(SONG_DIR).exists() is True
#    assert Path(BACKUPDIR).exists() is True

# command script existence
def test_scripts():
    assert Path(MOVE_SCRIPT).exists() is True
    assert Path(BACKUP_SCRIPT).exists() is True
    assert Path(SCRAPE_SCRIPT).exists() is True

# python modules existence
def test_modules():
    assert Path(SCRAPE_CATEGORIES).exists() is True
    assert Path(SCRAPE_ARTISTS).exists() is True
    assert Path(SCRAPE_SONGS).exists() is True
    assert Path(SCRAPE_LYRICS).exists() is True

# website access
def test_website():
    resp = requests.get(HOME_PAGE)
    assert resp.status_code is 200

# check the path strings...
