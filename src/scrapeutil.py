#!/usr/bin/env python3.7
# scrapeutil.py
"""Utility module Lyric Scraper program."""

# stand lib
import json
from pathlib import Path
import re
import re
import subprocess as sp
from time import sleep
from typing import Any
from typing import List
from typing import Set
from typing import Text
from typing import Tuple
from urllib.parse import unquote

# 3rd party
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

# custom
from constants import HOME_PAGE
from constants import PUNCTUATION
from constants import SLEEP_TIME
from constants import SONG_FIN

filter_ = SoupStrainer("a")


def buttontest() -> None:
    """Print test message. Returns None."""
    print("Button works")
    return None


def count_artists(dir_: Text) -> int:
    """Counts unique artist links. Returns Integer."""
    total = 0
    for x in Path(dir_).iterdir():
        if str(x).endswith("txt"):
            total += count_unique_lines(str(x))
    return total


def count_lines(file_: Text) -> int:
    """Counts lines in 'file_'. Returns Integer."""
    count = 0
    with open(file_, "r") as f:
        for line in f.readlines():
            count += 1
            print('\r%s %s' % (count, "lines"), end='\r')
    print()
    return count


def count_unique_lines(file_: Text) -> int:
    """Counts unique lines in 'file_'. Returns Integer."""
    with open(file_, "r") as f:
        return len(set(f.readlines()))


def get_artist(soup: Any) -> Text:
    """Extracts the artist's name. Returns String."""
    name_element = soup.h3.a
    return name_element.get_text()


def get_links(soup: Any, string: Text) -> Any:
    """Gets hrefs containing 'string' from 'soup'. Returns List."""
    return soup.find_all(href=re.compile(string))


def get_lyrics(soup: Any) -> Text:
    """Extract the lyrics from 'soup'. Returns String."""
    lyric_body = soup.find(id="lyric-body-text")
    return lyric_body.get_text()


# def get_hrefs(string: Text) -> Any:
def get_hrefs(hrefs: Set[Any]) -> Any:
    """Gets hrefs. Returns List."""
    return hrefs.find_all(href=re.compile(hrefs))


def get_song(soup: Any) -> Text:
    """Extracts the song's name. Returns String."""
    name_element = soup.find(id="lyric-title-text")
    return remove_slash(name_element.get_text())


def get_soup(link: Text, filter_: Any = None) -> Any:
    """Gets soup from a link. Returns BeautifulSoup object."""
    request = persistent_request(link)
    return BeautifulSoup(request.content, "html.parser", 
        parse_only=filter_)


def ensure_exists(string: Text) -> None:
    """Makes 'string' dir if doesn't exist. Returns None."""
    if not Path(string).exists():
        Path(string).mkdir()
    return None

 
def file_gen(file_: Text) -> Any:
    """Make a generator of a text file. Returns Generator."""
    with open(SONG_FIN) as song_list:
        for link in song_list.readlines():
            yield link.strip()


def format_artist_link(href: Any) -> Text:
    """Formats URL for the artist. Returns String."""
    return HOME_PAGE+"/"+href.get("href")


def format_artist_name(name: Text) -> Text:
    """Formats the artist's name. Returns String."""
    artist = unquote(name)
    artist = artist.replace("+", " ")
    artist = artist.replace("/", " ")
    return artist


def format_file_name(artist: Text, song: Text) -> Text:
    """Assembles basic file name. Returns String."""
    return artist + "_" + song + ".txt"


def format_song_name(link: Any) -> Text:
    """Formats the song's name. Returns String."""
    song = unquote(Path(link.get("href")).parts[4])
    song = song.replace("+", " ")
    song = song.replace("-", " ")
    return song


def load_categories(paths: Text) -> List[Text]:
    """Loads artists file names. Returns List."""
    temp = []
    for file_ in Path(paths).iterdir():
        temp.append(str(file_))
    temp.sort() 
    return temp


def load_file_list(file_: Text) -> List[Text]:
    """Loads 'file_'. Returns List."""
    temp = []
    total = count_lines(file_)
    loaded = 0
    with open(file_, "r") as f:
        for line in f.readlines():
            temp.append(line.strip())
            loaded += 1
    return temp


def load_json(file_path: Text) -> Any:
    """Loads a json file. Returns Json object."""
    with open(file_path) as file_obj:
        artist_list = json.loads(file_obj.read())
    return artist_list 


def persistent_request(link: Text) -> Any:
    """Persistently makes a request. Returns Request object."""
    request = simple_request(link)
    if not request.status_code == 200:
        return three_requests(link)
    return request


def progress_bar(iteration: int,
                 total: int,
                 prefix: Text = 'Todo:',
                 suffix: Text = '',
                 decimals: int = 1,
                 length: int = 100,
                 fill: Text = '█') -> None:
    """
    Call in a loop to create terminal progress bar. Returns None.
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
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration is total: 
        print()
    return None


def remove_punctuation(name: Text) -> Text:
    """Removes punctuation from song. Returns String."""
    no_punct = []
    for character in name:
        if character not in PUNCTUATION:
            no_punct.append(character)
    return ''.join(no_punct)


def remove_slash(string: Text) -> Text:
    """Removes the forward slash. Returns String."""
    temp = []
    for c in string:
        if c is not "/":
            temp.append(c)
    return "".join(temp)


def save(list_: List[Text], location: Text) -> None:
    """Writes 'list_' to 'location' as txt file. Returns None."""
    with open(location, "w+") as f:
        for element in sorted(list_):
            f.write(element+"\n")
    return None


def save_append(list_: Text, location: Text) -> None:
    """Appends 'list_' to 'location' as txt file. Returns None."""
    with open(location, "a+") as f:
        for element in list_:
            f.write(element+"\n")
    return None


def save_append_line(string: Text, location: Text) -> None:
    """Appends 'string' to location's text file. Returns None."""
    with open(location, "a+") as f:
        f.write(string+"\n")
    return None


def save_json(json_obj: Text, file_name: Text) -> None:
    """Saves 'json_obj' to 'file_name'. Returns None."""
    dumping = json.dumps(json_obj, sort_keys=True, indent=4)
    with open(file_name, "a+") as file_obj:
        file_obj.write(dumping)
    return None


def save_lyrics(list_: List[Text], location: Text) -> None:
    """Writes 'list_' to 'location' as txt file. Returns None."""
    with open(location, "w+") as f:
        for element in list_:
            f.write(element+"\n")
    return None


def scrape_setup(cur_todo: Text,
                 cur_fin: Text) -> Tuple[List[Text], List[Text]]:
    """Determines which links need to be scraped. 
        needs;
            - current todo file
            - current stage finished file
        Returns 2 Lists."""
    todo = set(load_file_list(cur_todo))
    finished = set(load_file_list(cur_fin))
    todo_len = len(todo)
    finished_len = len(finished)
    completed = 0
    diff = todo.difference(finished)
    print("Unique todos:", len(diff))
    

#     for el in finished:
#         try:
#             todo.remove(el)
#         except:
#             pass
#         completed += 1

#     return (todo, finished)
    return (list(diff), list(finished))

# remove?
def scrape_setup_song(prev_stage_dir: Text,
                      cur_fin: Text) -> Tuple[List[Text], List[Text]]:
    """Determines which links need to be scraped. 
        needs;
            - current todo file
            - current stage finished file. 
        Returns 2 Lists."""
    prev_fin = []
    for file_ in Path(prev_stage_dir).iterdir():
        prev_fin += load_file_list(str(file_))
    prev_fin = set(prev_fin)
    finished = set(load_file_list(cur_fin))
    return (list(prev_fin.difference(finished)), list(finished))


def simple_request(link: Text) -> Any:
    """Make an http request. Returns HttpResponse."""
    return requests.get(link)


def three_requests(link: Text) -> Any:
    """Makes up to 3 request attempts. Returns HttpResponse."""
    errors = 0
    request = simple_request(link)
    while request.status_code != 200 and errors < 3:
        print("BACKING OFF {0} :: {1}".format(SLEEP_TIME, link))
        errors += 1
        sleep(SLEEP_TIME)
        request = simple_request(link)
        if request.status_code == 200:
            break
    return request
