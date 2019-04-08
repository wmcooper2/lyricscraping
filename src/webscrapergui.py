#!/usr/bin/env python3.7
# webscrapergui.py
"""A GUI tool for webscraping lyrics from 'www.lyrics.com'."""
# stand lib
from pathlib import Path
import tkinter as tk
from tkinter import ttk

# custom
from constants import ARTIST_ERRORS
from constants import ALL_LYRICS_FILES
from constants import ARTIST_DIR
from constants import CATEGORY_ERRORS
from constants import CATEGORY_FIN
from constants import CATEGORY_TODO
from constants import HOME_PAGE
from constants import LYRIC_ERRORS
from constants import SONG_ERRORS
from constants import SONG_FIN
from constants import WIDTH
from directorysetup import *
from scrapeutil import count_all_lines
from scrapeutil import count_files
from scrapeutil import count_unique_lines
import scrapecategories as sc
import scrapeartists as sa
import scrapesongs as ss
import scrapelyrics as sl


def redraw_category_values():
    """Redraws the category values. Returns None."""
    c_total = ttk.Label(status_frame, 
        text=str(count_unique_lines(CATEGORY_TODO)))
    c_total.grid(column=2, row=1, pady=6, padx=6)
    c_errors = ttk.Label(status_frame, 
        text=str(count_unique_lines(CATEGORY_ERRORS)))
    c_errors.grid(column=1, row=1, pady=6, padx=6)


def redraw_artist_values():
    """Redraws the artist values. Returns None."""
    a_total = ttk.Label(status_frame, 
        text=str(total))
    a_total.grid(column=2, row=2, pady=6, padx=6)
    a_errors = ttk.Label(status_frame, 
        text=str(total))
    a_errors.grid(column=1, row=2, pady=6, padx=6)


directory_setup()
win = tk.Tk()
win.title("Webscraping Lyrics")

main_box = ttk.Frame(win)
main_box.grid(column=0, row=0, pady=6, padx=6)

address_fr = ttk.LabelFrame(main_box, text="Target", width=L_WIDTH)
address_fr.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)
address = ttk.Label(address_fr, text=HOME_PAGE)
address.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)

status_frame = ttk.LabelFrame(main_box)
status_frame.grid(column=0, row=1, pady=6, padx=6)

# headers row
header1 = ttk.Label(status_frame, text="Stages")
header1.grid(column=0, row=0, pady=6, padx=6)
header2 = ttk.Label(status_frame, text="Errors")
header2.grid(column=1, row=0, pady=6, padx=6)
header3 = ttk.Label(status_frame, text="Totals")
header3.grid(column=2, row=0, pady=6, padx=6)

# buttons, left column
c_btn = ttk.Button(status_frame, text="Category", 
    command=sc.scrape)
c_btn.grid(column=0, row=1, pady=6, padx=6)
a_btn = ttk.Button(status_frame, text="Artist", 
    command=sa.scrape)
a_btn.grid(column=0, row=2, pady=6, padx=6)
s_btn = ttk.Button(status_frame, text="Song", 
    command=ss.scrape)
s_btn.grid(column=0, row=3, pady=6, padx=6)
l_btn = ttk.Button(status_frame, text="Lyric", 
    command=sl.scrape)
l_btn.grid(column=0, row=4, pady=6, padx=6)

# errors column
c_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(CATEGORY_ERRORS)))
c_errors.grid(column=1, row=1, pady=6, padx=6)

a_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(ARTIST_ERRORS)))
a_errors.grid(column=1, row=2, pady=6, padx=6)

s_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(SONG_ERRORS)))
s_errors.grid(column=1, row=3, pady=6, padx=6)

l_errors = ttk.Label(status_frame, 
    text=str(count_all_lines(LYRIC_ERRORS)))
l_errors.grid(column=1, row=4, pady=6, padx=6)

# totals column
c_total = ttk.Label(status_frame, 
    text=str(count_all_lines(CATEGORY_FIN)))
c_total.grid(column=2, row=1, pady=6, padx=6)

a_total = ttk.Label(status_frame, 
    text=str(sa.count_artists(ARTIST_DIR)))
a_total.grid(column=2, row=2, pady=6, padx=6)

# tempfix
s_total = ttk.Label(status_frame, 
    text=str(count_all_lines(SONG_FIN)))
s_total.grid(column=2, row=3, pady=6, padx=6)

# tempfix
l_total = ttk.Label(status_frame, 
    text=str(count_files(ALL_LYRIC_FILES)))
l_total.grid(column=2, row=4, pady=6, padx=6)
