#!/usr/bin/env python3
"""Extract the lyrics and save the text to a file."""

#stand lib
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
from scrapeutil import *

filter_ = SoupStrainer("a")

def get_song(soup):
    """Extracts the song's name. Returns String."""
    name_element = soup.find(id="lyric-title-text")
    return remove_slash(name_element.get_text())

def get_artist(soup):
    """Extracts the artist's name. Returns String."""
    name_element = soup.h3.a
    return name_element.get_text()

def get_lyrics(soup):
    """Extract the lyrics from 'soup'. Returns String."""
    lyric_body = soup.find(id="lyric-body-text")
    return lyric_body.get_text()

#def save_lyrics(artist, song_name, lyrics):
#    """Writes lyrics to the artist's folder. Returns None."""
#    file_name = RESULTS+artist+"_"+song_name+".txt"
#    with open(file_name, "w+") as file_:
#        file_.write(str(lyrics))

def remove_slash(string):
    """Removes the forward slash. Returns String."""
    temp = []
    [temp.append(c) for c in string if c is not "/"]
    return "".join(temp)

def file_gen(file_):
    """Make a generator of a text file. Returns Generator."""
    with open(SONG_FILE) as song_list:
        for link in song_list.readlines():
            yield link.strip()

def format_file_name(artist, song):
    """Makes the file name for the lyrics file. Returns String."""
    return artist+"_"+song_name+".txt"





#Main
def scrape(link):
    """A single scraping attempt of 'link'. Returns None."""
    print("--- LYRIC SCRAPING; STARTED ---")

    #rename scrape_setup_artist 
    todo, finished = scrape_setup_artist(SONG_FIN, LYRIC_ERRORS, LYRIC_FIN)
    print("finished::", len(finished))
    print("todo    ::", len(todo))

#    gen = file_gen(SONG_FILE)
#    for link in gen:

    counter = 0
    for link in LYRIC_TODO:
        counter += 1
        try:
            soup    = get_soup(link)
            lyrics  = get_lyrics(soup)
            song    = get_song(soup)
            artist  = get_artist(soup)
            lyric_file = format_file_name(artist, song)
            save(lyrics, RESULTS+lyric_file)
            save_append_line(link, LYRIC_FIN)
            if len(todo) % 100 == 0:
                total = len(todo) + len(finished)
                progress = len(finished) + counter
                print("Progress::", str(round(progress/total, 4), "%")

            #get the first letter of the artist name
            #make a dir with the first letter of the artist name
                #if the first letter is not a letter (a symbol):
                    #save the lyrics to the symbol dir
                #else:
                    #save to the dir that has the same first letter
        except:
            print("Error::", link)
            save_append_line(error, LYRIC_ERRORS)
    print("--- LYRIC SCRAPING; FINISHED ---")

if __name__ == "__main__":
    scrape()
