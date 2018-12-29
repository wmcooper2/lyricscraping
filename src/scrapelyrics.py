#!/usr/bin/env python3
"""Extract the lyrics and save the text to a file."""

#stand lib
import logging
from pathlib import Path
from time import time
from time import sleep
from urllib.parse import unquote

#3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

#custom
from constants import *
from scrapeutil import get_soup
from scrapeutil import persistent_request

SAVE_DIR        = CWD+"/alllyrics/"
filter_ = SoupStrainer("a")
logging.basicConfig(filename=LYRIC_ERRORS, level=logging.INFO, format="")

def extract_song_name(soup):
    """Extracts the song's name. Returns String."""
    name_element = soup.find(id="lyric-title-text")
    name = name_element.get_text()
    return remove_slash(name) #removes forward slash

def extract_artist_name(soup):
    """Extracts the artist's name. Returns String."""
    name_element = soup.h3.a
    name = name_element.get_text()
    return name

def extract_lyrics(song_soup):
    """Extract the lyrics from the soup. Returns String."""
    lyric_body = song_soup.find(id="lyric-body-text")
    return lyric_body.get_text()

def save_lyrics(artist, song_name, lyrics):
    """Writes lyrics to the artist's folder. Returns None."""
    file_name = SAVE_DIR+artist+"_"+song_name+".txt"
    with open(file_name, "w+") as file_:
        file_.write(str(lyrics))

def remove_slash(string):
    """Removes the forward slash. Returns String."""
    no_slashes = []
    for character in string:
        if character not in "/": 
            no_slashes.append(character)
    return "".join(no_slashes)

def count_lines(text_file):
    """Get a count of the links in the song file. Returns Integer."""
    with open(text_file, "r") as file_:
        return len(file_.readlines())

def file_gen(file_):
    """Make a generator of a text file. Returns Generator."""
    with open(SONG_FILE) as song_list:
        for link in song_list.readlines():
            yield link.strip()

#Main
# use single_scrape in error recovery
def single_scrape(link):
    """A single scraping attempt of 'link'. Returns None."""
    try:
        soup = get_soup(link)
        song_name = extract_song_name(soup)
        artist = extract_artist_name(soup)
        lyrics = extract_lyrics(soup)
        save_lyrics(artist, song_name, lyrics)
        print("DONE::", link)
    except:
        print("ERROR::", link)
        #temporary, replace with logging when finished first round
#        logging.info(link)
        with open(LYRIC_ERRORS, "a+") as error_file:
            error_file.write(link)
            error_file.write("\n")

def scrape_everything():
    SONG_TOTAL = count_lines(SONG_FILE)
    gen = file_gen(SONG_FILE)
    for link in gen:
        single_scrape(link)

if __name__ == "__main__":
    scrape_everything()
    print("JOB FINISHED")
