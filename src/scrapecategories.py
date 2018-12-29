"""Scrapes category links."""
#stand lib
from pathlib import Path
from pprint import pprint
import re
from time import sleep

#3rd party
from bs4 import BeautifulSoup
import requests

#custom
from constants import *
from scrapeutil import *

#dont need logging here? what about error recovery script?

def category_file():
    """Loads category links from text file. Returns List."""
    temp = []
    with open(CATEGORY_FILE, "r") as file_obj:
        for line in file_obj.readlines():
            temp.append(line.strip())
    return temp

def error_recovery(link):
    """unfinished"""
    pass

def single_scrape(link):
    """Place holder"""
    pass

# Main function, call from external scripts
def scrape():
    print("--- CATEGORY SCRAPING STARTED ---")
    print("Scraping from ::", HOME_PAGE)
    
    soup = get_soup(HOME_PAGE)
    category_links = get_links(soup, "^/artists/")
    a_tags = set(category_links)
    hrefs = get_hrefs(a_tags)
    suffixed = add_suffixes(hrefs, "/99999")
    categories = add_prefixes(suffixed, HOME_PAGE)
    save(categories, CATEGORY_FILE)

    #when/where are the errors saved?

    print("--- CATEGORY SCRAPING FINISHED ---")

if __name__ == "__main__":
    scrape()
