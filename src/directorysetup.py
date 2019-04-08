#!/usr/bin/env python3.7
# directorysetup.py
"""Directory setup for Lyric program.
    Creates files and directories in '<programroot>/src/'.
"""
# stand lib
from pathlib import Path

# custom
from constants import DIRS
from constants import FILES


def check(paths: List[str]) -> bool:
    """Checks that all paths exist. Returns Boolean."""
    return all([Path(x).exists() for x in paths])


def dir_file_setup(paths: str) -> None:
    """Makes dirs and files. Returns None."""
    for x in paths:
        if not Path(x).exists(): 
            setup(Path(x))
            print("Created:", Path(x))
        else: 
            pass
    return None


def directory_setup(paths: List[str]) -> None:
    """Creates dirs files that don't exist. Returns None."""
    if check(paths):
        print("All dirs and files are in place.")
    else:
        dir_file_setup(paths)
    return None


def setup(path: str) -> None:
    """Creates 'path'. Returns None."""
    if str(path).endswith("txt"):
        path.touch()
    else:
        path.mkdir()
    return None


if __name__ == "__main__":
    print("--- DIRECTORY/FILE CHECK, STARTED ---")
    directory_setup(DIRS+FILES)
    print("--- DIRECTORY/FILE CHECK, FINISHED ---")
