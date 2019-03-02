"""Directory setup for Lyric program.
    Creates files and directories in '<programroot>/src/'.
"""
#stand lib
from pathlib import Path

#custom
from constants import *

dirs = [
    SUPPORT,
    RESULTS,
    CATEGORY_DIR,
    ARTIST_DIR,
    SONG_DIR,
    LYRIC_DIR
]

files = [
    CATEGORY_ERRORS,
    CATEGORY_FIN,
    ARTIST_ERRORS,
    ARTIST_FIN,
    SONG_ERRORS,
    SONG_FIN,
    LYRIC_ERRORS,
    LYRIC_TODO
]

def check(list_):
    """Checks that all paths in 'list_' exist.
        Returns Boolean."""
    return all([Path(x).exists() for x in list_])

#def message(path):
#    """Displays 'created' message in Terminal. Returns None."""
#    print("created: ", str(path))

def setup(path):
    """Makes path. Returns None."""
    if str(path).endswith("txt"):   path.touch()
    else:                           path.mkdir()

def dir_file_setup(list_):
    """Makes dirs and files. Returns None."""
    for x in list_:
        if not Path(x).exists(): 
            setup(Path(x))
            print("Created:", Path(x))
        else: 
            print("Exists: ", x)

def directory_setup():
    """Runs a check on the program's dirs and files. 
        Creates dirs files that don't exist.
        Returns None."""
    print("--- DIRECTORY/FILE CHECK, STARTED ---")
    if check(dirs+files):   print("All dirs and files are in place.")
    else:                   dir_file_setup(dirs+files)
    print("--- DIRECTORY/FILE CHECK, FINISHED ---")

#Main
if __name__ == "__main__":
    directory_setup()
