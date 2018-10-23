#!/usr/bin/env python3
""" Uses the artist links generated from scrapeartists.py to scrape song 
    links from each artist's link.
"""
#unfinished; save text file version of song link list

#stand lib
import json
import logging
from pathlib import Path
from time import sleep
from urllib.parse import unquote

#3rd party
from bs4 import BeautifulSoup
import requests

#custom
from constants import *
from scrapeutil import get_links
from scrapeutil import get_soup
from scrapeutil import load_json
from scrapeutil import persistent_request
from scrapeutil import save_json

logging.basicConfig(filename=SONG_ERRORS, level=logging.INFO, format="")

def get_artist():
    """Gets an artist from the json file. Returns Generator"""
    pass

def load_categories(dir_):
    """Loads the file names for the lists of artists. Returns List."""
    temp = []
    for file_ in Path(dir_).iterdir():
        temp.append(str(file_))
    temp.sort() 
    return temp

def remove_punctuation(song_name):
    """Removes punctuation from song_name. Returns String."""
    no_punct = []
    for character in song_name:
        if character not in PUNCTUATION:
            no_punct.append(character)
    return ''.join(no_punct)

def format_artist_name(name):
    """Formats the artist's name. Returns String."""
    artist = unquote(name)
    artist = artist.replace("+", " ")
    artist = artist.replace("/", " ")
    return artist

def format_song_name(link):
    """Formats the song's name. Returns String."""
    song = unquote(Path(link.get("href")).parts[4])
    song = song.replace("+", " ")
    song = song.replace("-", " ")
    return song

def save_stats(name, count):
    """Save artist's song count to text file. Returns None."""
    with open(ARTIST_STATS, "a+") as file_obj:
        stat = name+" :: "+str(count)+" songs"
        file_obj.write(stat)
        file_obj.write("\n")

#Main
# call single_scrape in error recovery
def single_scrape(category):
    """A single scraping attempt of 'category'. Returns None."""
    artist_list = load_json(category)
    for artist_name, link in artist_list.items():
        song_count = 0
        soup = get_soup(link)
        song_links = get_links(soup, "^/lyric/")
        song_dict = {}
        for link in song_links:
            song_count += 1
            try:
                song = format_song_name(link)
                full_song_link = HOME_PAGE+link.get("href")
                song_dict[song] = full_song_link
            except:
                print("ERROR ::", link)
                logging.info(link)

        artist = format_artist_name(artist_name)
        json_name = SONG_DIR+artist+"_Songs.json"
        save_json(song_dict, json_name)

        print("SCRAPED ::", artist)

def scrape_everything():
    categories = load_categories(ARTIST_DIR)
    for category in categories:
        print("CATEGORY STARTED ::", category)
        artist_list = load_json(category)
        print("CATEGORY FINISHED ::", category)

if __name__ == "__main__":
    print("--- SONG SCRAPING, START ---")
#    scrape_everything()
    single_scrape("/Volumes/YUUSHI/allartists/TESTjson.txt")
    print("--- SONG SCRAPING, FINISHED ---")
