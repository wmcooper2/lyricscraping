#!/usr/bin/env python3.7
# scrapelyrics.py
"""Scrapes lyrics. Step 4."""

# stand lib
from pathlib import Path
from string import ascii_uppercase as UPPERS
from time import time
from time import sleep
from typing import Any
from urllib.parse import unquote

# 3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

# custom
from constants import DEBUG
from constants import LYRIC_DIR
from constants import LYRIC_FIN
from constants import LYRIC_ERRORS
from constants import LYRIC_TODO
from scrapeutil import ensure_exists
from scrapeutil import filter_
from scrapeutil import format_file_name
from scrapeutil import get_artist
from scrapeutil import get_lyrics
from scrapeutil import get_song
from scrapeutil import get_soup
from scrapeutil import progress_bar
from scrapeutil import save_append_line
from scrapeutil import save_lyrics
from scrapeutil import scrape_setup

# import pdb

def scrape() -> None:
    """A single scraping attempt of 'link'. Returns None."""
    print("--- LYRIC SCRAPING; STARTED ---")
    print("Loading unfinished work...")
    todo, finished = scrape_setup(LYRIC_TODO, LYRIC_FIN)
    fin_len = len(finished)
    todo_len = len(todo)

    completed = 0
    for link in todo:
        try:
            soup = get_soup(link)
            song = get_song(soup)
            artist = get_artist(soup)
            file_name = format_file_name(artist, song)
            
            #final clean up of lyrics
            lyrics = get_lyrics(soup)
            lyrics = list(lyrics.split("\n"))
            lyrics = list(map(lambda x: x.strip(), lyrics))
            save_append_line(link, LYRIC_FIN)

            letter = artist[0]
            save_path = LYRIC_DIR+letter+"lyrics/"
            ensure_exists(save_path)

            if letter in UPPERS:
                save_lyrics(lyrics, save_path+file_name)
            else:
                symbol_dir = LYRIC_DIR+"symbollyrics/"
                save_lyrics(lyrics, symbol_dir+file_name)
        except AttributeError:
            save_append_line(link, LYRIC_ERRORS)
        except KeyboardInterrupt:
            print("Stopped manually.")
            quit()
        completed += 1
        print('\r%s %s' % (completed, "lyrics"), end='\r')
    return None


if __name__ == "__main__":
    scrape()
