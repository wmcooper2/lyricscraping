#!/usr/bin/env python3
"""This module scrapes for the category links."""

#stand lib
from pathlib import Path
import re
from time import sleep

#3rd party
from bs4 import BeautifulSoup
import requests

#custom
from constants import *
from scrapeutil import get_links
from scrapeutil import get_soup
from scrapeutil import persistent_request
from scrapeutil import save_list

#dont need logging here? what about error recovery script?

def add_suffixes(list_obj, suffix):
    """Appends 'suffix' to all elements in 'list_obj'. Returns List."""
    temp = []
    for each in list_obj:
        temp.append(each + suffix)
    return temp

def add_prefixes(list_obj, prefix):
    """Prepends 'prefix' to all elements in 'list_obj'. Returns List."""
    temp = []
    for each in list_obj:
        temp.append(prefix + each)
    return temp
 
#replace with set?
def remove_duplicate_links(list_obj):
    """Removes duplicate links. Returns List."""
    temp = []
    for link in list_obj:
        letter_category = link.get("href")
        if letter_category not in temp:
            temp.append(letter_category)
    return temp

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
def scrape_everything():
    soup = get_soup(HOME_PAGE)
    category_links = get_links(soup, "^/artists/")
    category_names = remove_duplicate_links(category_links)
    suffixed_categories = add_suffixes(category_names, "/99999")
    categories = add_prefixes(suffixed_categories, HOME_PAGE)
    save_list(categories, CATEGORY_FILE)

if __name__ == "__main__":
    print("--- CATEGORY SCRAPING STARTED ---")
    print("Scraping from ::", HOME_PAGE)
    scrape_everything()
    print("--- CATEGORY SCRAPING FINISHED ---")
