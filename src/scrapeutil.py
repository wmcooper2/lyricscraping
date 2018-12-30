"""Utility module Lyric Scraper program."""
#stand lib
from glob import glob
import json
from pathlib import Path
import re
import subprocess as sp
from time import sleep

#3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

#custom
from constants import *

filter_ = SoupStrainer("a")

def simple_request(link):
    """Makes only one request attempt. Returns Request object."""
    return requests.get(link)
    
def three_requests(link):
    """Makes up to 3 request attempts. Returns Request object."""
    errors = 0
    request = simple_request(link)
    while request.status_code != 200 and errors < 3:
        print("BACKING OFF {0} :: {1}".format(SLEEPTIME, link))
        errors += 1
        sleep(SLEEPTIME)
        request = simple_request(link)
        if request.status_code == 200:
            break
    return request

def persistent_request(link):
    """Persistently makes a request. Returns Request object."""
    request = simple_request(link)
    if not request.status_code == 200:
        return three_requests(link)
    return request

def get_links(soup, string):
    """Gets hrefs containing 'string' from 'soup'. Returns List."""
    return soup.find_all(href=re.compile(string))

def get_hrefs(linklist):
    """Gets all href values from 'linklist'. Returns List."""
    return list(map(lambda link: link.get("href"), linklist))

def get_soup(link, filter_=None):
    """Gets soup from a link. Returns BeautifulSoup object."""
    request = persistent_request(link)
    return BeautifulSoup(request.content, "html.parser", 
        parse_only=filter_)

#test manually, for now
def save(list_, location):
    """Writes 'list_' to 'location' as txt file. Returns None."""
    with open(location, "w+") as f:
        for element in sorted(list_):
            f.write(element)
            f.write("\n")

def save_append_line(string, location):
    """Appends 'string' to location's text file. Returns None."""
    with open(location, "a+") as f:
        f.write(string)
        f.write("\n")

#test manually, for now
def save_append(list_, location):
    """Appends 'list_' to 'location' as txt file. Returns None."""
    with open(location, "a+") as f:
        for element in list_:
            f.write(element)
            f.write("\n")

#test manually, for now
def save_json(json_obj, file_name):
    """Saves 'json_obj' to 'file_name'. Returns None."""
    dumping = json.dumps(json_obj, sort_keys=True, indent=4)
    with open(file_name, "a+") as file_obj:
        file_obj.write(dumping)

#test manually, for now
def load_json(file_path):
    """Loads a json file. Returns Json object."""
    with open(file_path) as file_obj:
        artist_list = json.loads(file_obj.read())
    return artist_list 

#def lines_in_file(file_):
def count_unique_lines(file_):
    """Counts unique lines in 'file_'. Returns Integer."""
    with open(file_, "r") as f:
        return len(set(f.readlines()))

def count_all_lines(file_):
    """Counts all lines in file_. Returns Integer."""
    with open(file_, "r") as f:
        return len(f.readlines())

#test manually, for now
def load_file_list(file_):
    """Loads 'file_'. Returns List."""
    temp = []
    with open(file_, "r") as f:
        for line in f.readlines():
            temp.append(line.strip())
    return temp

def count_files(dir_):
    """Counts files in 'dir_'. Returns Integer."""
    path = str(Path(dir_))
    cmd = "ls "+path+" | wc -l"
    return sp.run(cmd, encoding="utf-8", shell=True,
        stdout=sp.PIPE, stderr=sp.PIPE).stdout.strip()

#test manually, for now
def buttontest():
    """Prints test line to terminal. Returns None."""
    print("button works")

def format_artist_link(href):
    """Formats URL for the artist. Returns String."""
    return HOME_PAGE+"/"+href.get("href")

def scrape_setup_artist(prev_fin, cur_err, cur_fin):
    """Determines which links need to be scraped. 
        needs;
            - previous stage finished file
            - current stage error file
            - current stage finished file
        Returns 2 Lists."""
    todo = list(set(load_file_list(prev_fin)
                    +load_file_list(cur_err)))
    finished = load_file_list(cur_fin)
    [todo.remove(el) for el in finished]
    return todo, finished

def scrape_setup_song(prev_stage_dir, cur_err, cur_fin):
    """Determines which links need to be scraped. 
        needs;
            - current stage error file
            - current stage finished file. 
        Returns 2 Lists."""
    prev_fin = []
    for file_ in Path(prev_stage_dir).iterdir():
        prev_fin += list(set(load_file_list(str(file_))))
    todo = prev_fin + load_file_list(cur_err)
    finished = load_file_list(cur_fin)
    [todo.remove(el) for el in finished]
    return todo, finished




# works if Stop().stop_scraping is called, but not effective in tkinter for stopping a process/thread?
class Stop():
    stop = False
    def __init__(self):
        pass

    def stop_scraping(self):
        """Changes Stop class attribute to True. Returns None."""
        Stop.stop = True
        print("stopped")
