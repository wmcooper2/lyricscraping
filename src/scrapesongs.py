"""Scrape song links from www.lyrics.com"""
#stand lib
from pathlib import Path
from pprint import pprint
from urllib.parse import unquote

#custom
from constants import *
from scrapeutil import *

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


#Main
def scrape():
    """Main scraping function. Returns None."""
    print("--- SONG SCRAPING, START ---")
    todo, finished = scrape_setup_song(ARTIST_DIR, SONG_ERRORS, SONG_FIN)
    print("finished::", len(finished))
    print("todo    ::", len(todo))
    for thing in sorted(todo):
        try:
            soup = get_soup(thing)
            a_tags = get_links(soup, "^/lyric/")
            hrefs = get_hrefs(a_tags)
            links = list(map(lambda x: unquote(HOME_PAGE+x), hrefs))
            save_append(links, LYRIC_TODO)
            save_append_line(thing, SONG_FIN)
            print("Saved::", thing)
        except:
            print("Error::", thing)
            save_append_line(thing, SONG_ERRORS)
            pass

    #put a list set thing here, reload the files then...
    print("--- SONG SCRAPING, FINISHED ---")

if __name__ == "__main__":
    scrape() 
