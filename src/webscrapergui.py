#!/usr/bin/env python3
"""A GUI tool for webscraping lyrics from 'www.lyrics.com'."""

#stand lib
from pathlib import Path
import tkinter as tk
from tkinter import ttk

#custom
from constants import *
from directorysetup import *
from scrapeutil import *

import scrapecategories as sc
import scrapeartists as sa
import scrapesongs as ss
import scrapelyrics as sl

#def redraw_category_total(total):
#    """Redraws the category totals. Returns None."""
#    c_total = ttk.Label(status_frame, 
#        text=str(total))
#    c_total.grid(column=2, row=1, pady=6, padx=6)
#
#def redraw_category_errors(total):
#    """Redraws the category errors. Returns None."""
#    c_errors = ttk.Label(status_frame, 
#        text=str(total))
#    c_errors.grid(column=1, row=1, pady=6, padx=6)

def redraw_artist_total(total):
    """Redraws the artist totals. Returns None."""
    a_total = ttk.Label(status_frame, 
        text=str(total))
    a_total.grid(column=2, row=2, pady=6, padx=6)

def redraw_artist_errors(total):
    """Redraws the artist errors. Returns None."""
    a_errors = ttk.Label(status_frame, 
        text=str(total))
    a_errors.grid(column=1, row=2, pady=6, padx=6)

#def scrape_artists():
#    """Scrapes artists from www.lyrics.com"""
#    print("--- ARTIST SCRAPING STARTED ---")
#    cat_links = load_file_list(CATEGORY_FILE)
#    for link in cat_links:
#        soup = get_soup(link)
#        art_links = get_links(soup, "^artist")
#        category = Path(link).parts[3]
#        text_file = (ARTIST_DIR+category+"_"+"artistlinks.txt") 
#        long_list = list(map(format_artist_link, art_links))
#        save(long_list, text_file)
#        print("saved", text_file)
#    print("--- ARTIST SCRAPING FINISHED ---")

#Main
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

#headers row
header1 = ttk.Label(status_frame, text="Stages")
header1.grid(column=0, row=0, pady=6, padx=6)
header2 = ttk.Label(status_frame, text="Errors")
header2.grid(column=1, row=0, pady=6, padx=6)
header3 = ttk.Label(status_frame, text="Totals")
header3.grid(column=2, row=0, pady=6, padx=6)

#buttons, left column
c_btn = ttk.Button(status_frame, text="Category", 
    command=sc.scrape)
c_btn.grid(column=0, row=1, pady=6, padx=6)
a_btn = ttk.Button(status_frame, text="Artist", 
    command=sa.scrape)
a_btn.grid(column=0, row=2, pady=6, padx=6)
#working on this one



s_btn = ttk.Button(status_frame, text="Song", 
    command=buttontest)
s_btn.grid(column=0, row=3, pady=6, padx=6)
l_btn = ttk.Button(status_frame, text="Lyric", 
    command=buttontest)
l_btn.grid(column=0, row=4, pady=6, padx=6)

#errors column
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




#totals column
c_total = ttk.Label(status_frame, 
    text=str(count_all_lines(CATEGORY_FILE)))
c_total.grid(column=2, row=1, pady=6, padx=6)

a_total = ttk.Label(status_frame, 
    text=str(sa.count_artists()))
a_total.grid(column=2, row=2, pady=6, padx=6)

#tempfix
s_total = ttk.Label(status_frame, 
#    text=str(count_songs2()))
    text="na")
s_total.grid(column=2, row=3, pady=6, padx=6)

#tempfix
l_total = ttk.Label(status_frame, 
#    text=str(count_files(LYRIC_DIR)))
    text="na")
l_total.grid(column=2, row=4, pady=6, padx=6)



#rename/rework to "check" buttons?
#recover buttons
#c_recover = ttk.Button(status_frame, text="recover", 
#    command=buttontest)
#c_recover.grid(column=3, row=1, pady=6, padx=6)
#a_recover = ttk.Button(status_frame, text="recover", 
#    command=buttontest)
#a_recover.grid(column=3, row=2, pady=6, padx=6)
#s_recover = ttk.Button(status_frame, text="recover", 
#    command=buttontest)
#s_recover.grid(column=3, row=3, pady=6, padx=6)
#l_recover = ttk.Button(status_frame, text="recover", 
#    command=buttontest)
#l_recover.grid(column=3, row=4, pady=6, padx=6)

#bottom buttons
button_frame = ttk.LabelFrame(main_box)
button_frame.grid(column=0, row=2, sticky=tk.W, pady=6, padx=6)

#temp fix
stop_btn = ttk.Button(button_frame, text="Stop", 
    command=buttontest)
stop_btn.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)

win.mainloop()
