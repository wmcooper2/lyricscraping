#!/usr/bin/env python3
"""All of the steps combined to scrape from lyrics.com"""

#stand lib
import logging
from pathlib import Path
from urllib.parse import unquote

#3rd party
from bs4 import BeautifulSoup
import requests

#custom
from constants import *
from scrapeutil import get_links
from scrapeutil import get_soup
from scrapeutil import persistent_request
from scrapeutil import save_json
from scrapeutil import save_list

logging.basicConfig(filename=ARTIST_ERRORS, level=logging.INFO, format="")

def get_artist_info(string):
    """Gets Artist information from 'link'. Returns 2 Strings."""
    link = string.get("href")
    artist_link = HOME_PAGE+"/"+link
    artist_name = Path(link).parts[1]
    return unquote(artist_name), artist_link

def make_unique_set(list_obj):
    """Removes duplicate links. Returns List."""
    temp = []
    for link in list_obj:
        letter_category = link.get("href")
        if letter_category not in temp:
            temp.append(letter_category)
    return temp

def make_artist_dict(artists):
    """Pairs the artist's name with the artist's link. 
        Returns Dictionary."""
    artist_dict = {}
    for artist in artists:
        artist_name, link = get_artist_info(artist)
        artist_dict[artist_name] = link
    return artist_dict

def make_artist_list(artists):
    """Makes a list of links only. Returns List."""
    list_ = []
    for artist in artists:
        artist_name, link = get_artist_info(artist)
        list_.append(link)
    return list_

def load_category_links(location):
    """Loads category links from text file. Returns List."""
    temp = []
    with open(location, "r") as file_obj:
        for line in file_obj.readlines():
            temp.append(line.strip())
    return temp

#not used
def category_stats(list_obj, location):
    """Writes 'list_obj' to 'location'. Returns None."""
    with open(location, "a+") as file_obj:
        line = "Category "+list_obj[0]+" :: "+list_obj[1]+" Artists"
        file_obj.write(line)
        file_obj.write("\n")


#Main
#call this in error recovery
def single_scrape(link):
    """A single scraping attempt of 'link'. Returns None."""
    try:
        soup = get_soup(link)
        artist_links = get_links(soup, "^artist")
        category = Path(link).parts[3]

        #json file, artist name and link
        artists_dict = make_artist_dict(artist_links)
        json_file = ARTIST_DIR+"/Category_"+category+"_Artists_json.txt"
        save_json(artists_dict, json_file) 

        #plain text file, link only
        text_file = (ARTIST_DIR+"/Category_"+category
                               +"_Artists_linksonly.txt") 
        link_list = make_artist_list(artist_links)
        save_list(link_list, text_file)
        print("SCRAPED ::", link)

    except:
        print("ERROR::\t", link)
        logging.info(link)

def scrape_everything():
    category_links = load_category_links(CATEGORY_FILE)
    for link in category_links:
        single_scrape(link)

if __name__ == "__main__":
    print("--- ARTIST SCRAPING STARTED ---")
    scrape_everything()
    print("--- ARTIST SCRAPING FINISHED ---")
    #timetaken()
