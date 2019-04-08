#!/usr/bin/env python3.7
# scrapecategories.py
"""Scrapes category links."""
# stand lib
from pathlib import Path

# custom
from constants import CATEGORY_FIN
from constants import HOME_PAGE
from scrapeutil import get_soup
from scrapeutil import get_links
from scrapeutil import save

def scrape() -> None:
    print("--- CATEGORY SCRAPING STARTED ---")
    print("Scraping from:", HOME_PAGE)
    soup = get_soup(HOME_PAGE)
    category_links = get_links(soup, "^/artists/")
    a_tags = set(category_links)
    hrefs = get_hrefs(a_tags)
    suffixed = list(map(lambda x: x+"/99999", hrefs))
    prefixed = list(map(lambda x: HOME_PAGE+x, suffixed))
    save(prefixed, CATEGORY_FIN)
    print("--- CATEGORY SCRAPING FINISHED ---")

# if __name__ == "__main__":
#     scrape()
