#!/usr/bin/env python3
"""A utility module for webscraping lyrics."""

#stand lib
from glob import glob
import json
from pathlib import Path
import re
from time import sleep

#3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

#custom
from constants import *
import dirsandfiles_test as df

filter_ = SoupStrainer("a")

def persistent_request(link):
    """Makes a single request multiple times until successful.
    Returns Request object."""
    request = requests.get(link)
    if request.status_code == 200:
        return request
    else:
        errors = 0
        while request.status_code != 200 and errors < 3:
            print("BACKING OFF ::", link)
            errors += 1
            sleep(6)
            request = requests.get(link)
            if request.status_code == 200:
                break
        return request

def get_links(soup_obj, string):
    """Gets all hrefs containing 'string' from 'soup_obj'. Returns List."""
    return soup_obj.find_all(href=re.compile(string))

def get_soup(link, filter_=None):
    """Gets soup from a link. Returns BeautifulSoup object."""
    request = persistent_request(link)
    return BeautifulSoup(request.content, "html.parser", parse_only=filter_)

def save_list(list_, location):
    """Saves 'list_' contents to 'location' as plain text file.
        Returns None."""
    with open(location, "a+") as file_obj:
        for element in list_:
            file_obj.write(element)
            file_obj.write("\n")

def save_json(json_obj, file_name):
    """Saves 'json_obj' to 'file_name'. Returns None."""
    dumping = json.dumps(json_obj, sort_keys=True, indent=4)
    with open(file_name, "a+") as file_obj:
        file_obj.write(dumping)

def load_json(file_path):
    """Loads a json file. Returns Json object."""
    with open(file_path) as file_obj:
        artist_list = json.loads(file_obj.read())
    return artist_list 

def lines_in_file(file_):
    """Counts the unique lines in 'file_'. Returns Integer."""
    return len(set(open(file_).readlines()))

def count_songs():
    """Counts the lines in SONG_FILE. Returns Integer."""
    return lines_in_file(SONG_FILE) + lines_in_file(SONG_FILE2)

def count_songs2():
    """Counts the lines in SONG_SET_FILE. Returns Integer."""
    
    return sum(1 for line in set(open(SONG_SET_FILE, "r").readlines()))

def song_set():
    """Makes a set of song links and writes to a file. Returns None."""
    song_set = set()
#    (song_set.add(line) for line in open(SONG_FILE2, "r").readlines())
#    (song_set.add(line) for line in open(SONG_FILE, "r").readlines())
    for line in open(SONG_FILE2, "r").readlines():
        song_set.add(line)
    for line in open(SONG_FILE, "r").readlines():
        song_set.add(line)
    with open(SONG_SET_FILE, "w+") as song_set_file:
        for song in song_set:
            song_set_file.write(song)

def count_lyrics():
    """Counts the amount of lyrics files in LYRIC_DIR. Returns Integer."""
    lyrics_dirs = glob("/Volumes/YUUSHI/AllLyricscategory_*")
    temp_lyrics_dir = glob("/Volumes/YUUSHI/AllLyrics")
    total = 0
    for file_ in lyrics_dirs:
        total += sum(1 for line in Path(file_).iterdir())
    for file_ in temp_lyrics_dir:
        total += sum(1 for line in Path(file_).iterdir())
    for line in open(LYRIC_ERRORS, "r").readlines():
        total += 1
    return total

def button_test():
    """Prints test line to terminal. Returns None."""
    print("button works")

def run_test():
    """Runs the tests to ensure the program will run as expected.
        Returns None."""
    df.test_dirs()
    df.test_scripts()
    df.test_modules()
    df.test_website()
    print("All tests passed")
