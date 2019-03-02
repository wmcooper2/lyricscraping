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
format_file_name = lambda a, s: a+"_"+s+".txt"

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

#def format_file_name(artist, song):
#    """Makes the file name for the lyrics file. Returns String."""
#    return artist+"_"+song+".txt"

def show_progress(progress, total):
    """Draws lyric scraping progress to the terminal. Returns None."""
    print("{0} / {1}".format(str(progress), str(total)))

#Main
def scrape():
    """A single scraping attempt of 'link'. Returns None."""
    print("--- LYRIC SCRAPING; STARTED ---")
    print("Loading unfinished work...")
#    todo, finished = scrape_setup(SONG_FIN, LYRIC_ERRORS, LYRIC_FIN)
    todo, finished = scrape_setup(LYRIC_TODO, LYRIC_FIN)
    fin_len        = len(finished)
    todo_len       = len(todo)
    print("Finished:", fin_len)
    print("To do   :", todo_len)

    completed = 0
#    for link in load_file_list(LYRIC_TODO):
    for link in sorted(todo):
        completed += 1
        try:
            soup        = get_soup(link)
            song        = get_song(soup)
            artist      = get_artist(soup)
            file_name   = format_file_name(artist, song)
            
            #final clean up of lyrics
            lyrics  = get_lyrics(soup)
            lyrics  = list(lyrics.split("\n"))
            lyrics  = list(map(lambda x: x.strip(), lyrics))
            save_append_line(link, LYRIC_FIN)

            letter = artist[0]
            save_path = LYRIC_DIR+letter+"lyrics/"
            ensure_exists(save_path)

            if letter in UPPERS:
                save_lyrics(lyrics, save_path+file_name)
            else:
                symbol_dir = LYRIC_DIR+"symbollyrics/"
                save_lyrics(lyrics, symbol_dir+file_name)
        except:
            print("Error:", link)
            save_append_line(link, LYRIC_ERRORS)

        #user feedback
        if completed % 10 == 0:
            progress = fin_len  + completed
            #the math feels wrong
            total    = todo_len + fin_len
            show_progress(progress, total)

        if DEBUG:
            if completed >= 3:
                break

if __name__ == "__main__":
    scrape()
