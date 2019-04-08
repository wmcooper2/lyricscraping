#!/usr/bin/env python3.7
# scrapeartists.py
"""All of the steps combined to scrape from lyrics.com"""
# stand lib
from pathlib import Path
from pprint import pprint

# custom
from constants import ARTIST_DIR
from constants import CATEGORY_FIN
from constants import ARTIST_ERRORS
from constants import ARTIST_FIN
from scrapeutil import scrape_setup
from scrapeutil import count_unique_lines
from scrapeutil import get_links
from scrapeutil import format_artist_link
from scrapeutil import save


def count_artists(dir_: str) -> int:
    """Counts unique artist links. Returns Integer."""
    total = 0
    for x in Path(dir_).iterdir():
        if str(x).endswith("txt"):
            total += count_unique_lines(str(x))
    return total


def scrape() -> None:
    """Main scraping function. Returns None."""
    print("--- ARTIST SCRAPING STARTED ---")
    errors = []
    todo, finished = scrape_setup(CATEGORY_FIN, 
                                  ARTIST_ERRORS, 
                                  ARTIST_FIN)

    for cat in todo:
        try:
            soup = get_soup(cat)
            art_hrefs = get_links(soup, "^artist")
            art_links = list(map(format_artist_link, art_hrefs))
            category = Path(cat).parts[3]
            text_file = (ARTIST_DIR + category + "_" 
                         + "artistlinks.txt") 
            save(art_links, text_file)
            # progress_bar()
            finished.append(cat)
        except:
            errors.append(cat)
    save(errors, ARTIST_ERRORS)
    save(finished, ARTIST_FIN)
    print("--- ARTIST SCRAPING FINISHED ---")

# if __name__ == "__main__":
#     scrape()
