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
from scrapeutil import *
#from scrapeutil import get_links
#from scrapeutil import get_soup
#from scrapeutil import persistent_request
#from scrapeutil import save_json
#from scrapeutil import save



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


def make_artist_list2(artists):
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

def format_artist_link(artist):
    """Formats URL for the artist"""
    link = artist.get("href")
    return HOME_PAGE+"/"+link

#Main
#call this in error recovery
def single_scrape(link):
    """A single scraping attempt of 'link'. Returns None."""

#    except:
#        print("ERROR::\t", link)
#        logging.info(link)
    pass

def scrape():
    cat_links = load_file_list(CATEGORY_FILE)
    for link in cat_links:
        soup = get_soup(link)
        art_links = get_links(soup, "^artist")
        category = Path(link).parts[3]
        text_file = (ARTIST_DIR+category+"_"+"artistlinks.txt") 
        long_list = list(map(format_artist_link, art_links))
#        print(len(long_list), text_file)
        save(long_list, text_file)
        print("saved", text_file)
        #save to long list?

if __name__ == "__main__":
    print("--- ARTIST SCRAPING STARTED ---")
    scrape()
    print("--- ARTIST SCRAPING FINISHED ---")
