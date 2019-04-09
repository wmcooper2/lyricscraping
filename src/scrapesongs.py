#!/usr/bin/env python3.7
# scrapesongs.py
"""Scrapes song links. Step 3."""

# stand lib
from pathlib import Path
from pprint import pprint
from urllib.parse import unquote

# custom
from constants import ARTIST_DIR
from constants import HOME_PAGE
from constants import LYRIC_TODO
from constants import SONG_ERRORS
from constants import SONG_FIN
from scrapeutil import format_artist_name
from scrapeutil import format_song_name
from scrapeutil import get_hrefs
from scrapeutil import get_links
from scrapeutil import get_soup
from scrapeutil import load_categories
from scrapeutil import load_file_list
from scrapeutil import remove_punctuation
from scrapeutil import save
from scrapeutil import save_append
from scrapeutil import save_append_line
from scrapeutil import scrape_setup_song


def scrape() -> None:
    """Main scraping function. Returns None."""
    print("--- SONG SCRAPING, START ---")
    todo, finished = scrape_setup_song(ARTIST_DIR, SONG_FIN)
    print("Finished:", len(finished))
    print("To do   :", len(todo))

    errors = load_file_list(SONG_ERRORS)
    for thing in sorted(todo):
        try:
            soup = get_soup(thing)
            a_tags = get_links(soup, "^/lyric/")
            hrefs = get_hrefs(a_tags)
            links = list(map(lambda x: unquote(HOME_PAGE+x), hrefs))
            save_append(links, LYRIC_TODO)
            save_append_line(thing, SONG_FIN)
        except:
            errors.append(thing)

    save(list(set(errors)), SONG_ERRORS)
    print("--- SONG SCRAPING, FINISHED ---")

if __name__ == "__main__":
    scrape() 
