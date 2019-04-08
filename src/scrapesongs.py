#!/usr/bin/env python3.7
# scrapesongs.py
"""Scrape song links from www.lyrics.com"""
# stand lib
from pathlib import Path
from pprint import pprint
from urllib.parse import unquote

# custom
from constants import ARTIST_DIR
from constants import SONG_FIN
from constants import SONG_ERRORS
from constants import LYRIC_TODO
from constants import HOME_PAGE
from scrapeutil import get_soup
from scrapeutil import get_links
from scrapeutil import save_append_line


def load_categories(paths: str) -> List[str]:
    """Loads artists file names. Returns List."""
    temp = []
    for file_ in Path(paths).iterdir():
        temp.append(str(file_))
    temp.sort() 
    return temp


def remove_punctuation(name: str) -> str:
    """Removes punctuation from song. Returns String."""
    no_punct = []
    for character in name:
        if character not in PUNCTUATION:
            no_punct.append(character)
    return ''.join(no_punct)


def format_artist_name(name: str) -> str:
    """Formats the artist's name. Returns String."""
    artist = unquote(name)
    artist = artist.replace("+", " ")
    artist = artist.replace("/", " ")
    return artist


def format_song_name(link: Any) -> str:
    """Formats the song's name. Returns String."""
    song = unquote(Path(link.get("href")).parts[4])
    song = song.replace("+", " ")
    song = song.replace("-", " ")
    return song


#Main
def scrape() -> None:
    """Main scraping function. Returns None."""
    print("--- SONG SCRAPING, START ---")
    todo, finished = scrape_setup_song(ARTIST_DIR, SONG_FIN)
    print("Finished:", len(finished))
    print("To do   :", len(todo))

    errors = load_file_list(SONG_ERRORS)
    for thing in sorted(todo):
        try:
            soup = get_soup(thing)
            a_tags = get_links(soup, "^/lyric/")
            hrefs = get_hrefs(a_tags)
            links = list(map(lambda x: unquote(HOME_PAGE+x), hrefs))
            save_append(links, LYRIC_TODO)
            save_append_line(thing, SONG_FIN)
        except:
            errors.append(thing)

    save(list(set(errors)), SONG_ERRORS)
    print("--- SONG SCRAPING, FINISHED ---")

# if __name__ == "__main__":
#     scrape() 
