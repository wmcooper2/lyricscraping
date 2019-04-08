#!/usr/bin/env python3.7
# scrapeutil.py
"""Utility module Lyric Scraper program."""
# stand lib
import json
from pathlib import Path
import re
import subprocess as sp
from time import sleep

# 3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

# custom
from constants import *
from constants import SLEEPTIME

filter_ = SoupStrainer("a")


def buttontest() -> None:
    """Print test message. Returns None."""
    print("Button works")


# ???
def simple_request(l: Any) -> Any:
    """Not sure..."""
    return requests.get(l)


def count_files(dir_: Any) -> int:
    """Counts files in 'dir_'. Returns Integer."""
    path = str(Path(dir_))
    cmd = "ls "+path+" | wc -l"
    return sp.run(cmd, encoding="utf-8", shell=True,
        stdout=sp.PIPE, stderr=sp.PIPE).stdout.strip()


def count_unique_lines(file_):
    """Counts unique lines in 'file_'. Returns Integer."""
    with open(file_, "r") as f:
        return len(set(f.readlines()))


def count_all_lines(file_):
    """Counts all lines in file_. Returns Integer."""
    with open(file_, "r") as f:
        return len(f.readlines())
    

def ensure_exists(string):
    """Makes 'string' dir if doesn't exist. Returns None."""
    if not Path(string).exists():
        Path(string).mkdir()
    

def format_artist_link(href):
    """Formats URL for the artist. Returns String."""
    return HOME_PAGE+"/"+href.get("href")


def get_hrefs(linklist):
    """Gets all href values from 'linklist'. Returns List."""
    return list(map(lambda link: link.get("href"), linklist))


def get_links(soup, string):
    """Gets hrefs containing 'string' from 'soup'. Returns List."""
    return soup.find_all(href=re.compile(string))


def get_soup(link, filter_=None):
    """Gets soup from a link. Returns BeautifulSoup object."""
    request = persistent_request(link)
    return BeautifulSoup(request.content, "html.parser", 
        parse_only=filter_)


def load_file_list(file_):
    """Loads 'file_'. Returns List."""
    temp = []
    with open(file_, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp


def load_json(file_path):
    """Loads a json file. Returns Json object."""
    with open(file_path) as file_obj:
        artist_list = json.loads(file_obj.read())
    return artist_list 


def persistent_request(link):
    """Persistently makes a request. Returns Request object."""
    request = simple_request(link)
    if not request.status_code == 200:
        return three_requests(link)
    return request


def printProgressBar(iteration, total, prefix = '', suffix = '',
                     decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


def save(list_, location):
    """Writes 'list_' to 'location' as txt file. Returns None."""
    with open(location, "w+") as f:
        for element in sorted(list_):
            f.write(element+"\n")


def save_append_line(string, location):
    """Appends 'string' to location's text file. Returns None."""
    with open(location, "a+") as f:
        f.write(string+"\n")


def save_append(list_, location):
    """Appends 'list_' to 'location' as txt file. Returns None."""
    with open(location, "a+") as f:
        for element in list_:
            f.write(element+"\n")


def save_json(json_obj, file_name):
    """Saves 'json_obj' to 'file_name'. Returns None."""
    dumping = json.dumps(json_obj, sort_keys=True, indent=4)
    with open(file_name, "a+") as file_obj:
        file_obj.write(dumping)


def save_lyrics(list_, location):
    """Writes 'list_' to 'location' as txt file. Returns None."""
    with open(location, "w+") as f:
        for element in list_:
            f.write(element+"\n")


def scrape_setup(cur_todo, cur_fin):
    """Determines which links need to be scraped. 
        needs;
            - current todo file
            - current stage finished file
        Returns 2 Lists."""
    todo = list(set(load_file_list(cur_todo)))
    finished = load_file_list(cur_fin)
    for el in finished:
        try:
            todo.remove(el)
        except:
            pass
    return todo, finished


def scrape_setup_song(prev_stage_dir, cur_fin):
    """Determines which links need to be scraped. 
        needs;
            - current stage error file
            - current stage finished file. 
        Returns 2 Lists."""
    prev_fin = []
    for file_ in Path(prev_stage_dir).iterdir():
        prev_fin += load_file_list(str(file_))
    prev_fin = set(prev_fin)
    finished = set(load_file_list(cur_fin))
    return list(prev_fin.difference(finished)), list(finished)


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
