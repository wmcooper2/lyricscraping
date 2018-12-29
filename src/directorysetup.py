"""Directory setup for Lyric program.
    Creates files and directories in '<programroot>/src/'.
"""
#stand lib
from pathlib import Path

#custom
from constants import *

dirs = [
    CATEGORY_DIR,
    ARTIST_DIR,
    SONG_DIR,
    LYRIC_DIR
]

files = [
    CATEGORY_ERRORS,
    CATEGORY_FILE,
    CATEGORY_STATS,
    ARTIST_ERRORS,
    ARTIST_FILE,
    ARTIST_STATS,
    SONG_ERRORS,
    SONG_FILE,
    SONG_STATS,
    LYRIC_ERRORS,
    LYRIC_STATS
]

def check(list_):
    """Checks that all paths in 'list_' exist.
        Returns Boolean."""
    return all([Path(x).exists() for x in list_])

def message(path):
    """Displays 'created' message in Terminal. Returns None."""
    print("created: ", str(path))

def setup(path):
    """Makes path. Returns None."""
    if str(path).endswith("txt"): path.touch()
    else: path.mkdir()
    message(path)

def dir_file_setup(list_):
    """Makes dirs and files. Returns None."""
    for x in list_:
        if not Path(x).exists(): setup(Path(x))
        else: print("exists: ", x)

#Main
if __name__ == "__main__":
    print("--- DIRECTORY/FILE CHECK, START---")
    if check(dirs+files): print("All dirs and files are in place.")
    else: dir_file_setup(dirs+files)
    print("--- DIRECTORY/FILE CHECK, FINISH---")
