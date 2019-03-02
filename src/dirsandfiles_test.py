#!/usr/bin/env python3
"""Test module for the webscraping project"""

#stand lib
from pathlib import Path

#custom
from constants import *

def test_dirs():
    assert Path(CATEGORY_DIR).exists() is True
    assert Path(ARTIST_DIR).exists() is True
    assert Path(SONG_DIR).exists() is True

def test_modules():
    assert Path(SCRAPE_CATEGORIES).exists() is True
    assert Path(SCRAPE_ARTISTS).exists() is True
    assert Path(SCRAPE_SONGS).exists() is True
    assert Path(SCRAPE_LYRICS).exists() is True
