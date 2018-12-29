#!/usr/bin/env python3
"""A GUI tool for webscraping lyrics from 'www.lyrics.com'."""

#stand lib
from pathlib import Path
import tkinter as tk
from tkinter import ttk

#3rd party

#custom
from constants import *
import directorysetup as ds
import scrapecategories as sc
import scrapeartists as sa
import scrapesongs as ss
import scrapelyrics as sl
from scrapeutil import *

def redraw_category_total(total):
    """Redraws the category totals. Returns None."""
    c_total = ttk.Label(status_frame, 
        text=str(total))
    c_total.grid(column=2, row=1, pady=6, padx=6)

def redraw_category_errors(total):
    """Redraws the category totals. Returns None."""
    c_errors = ttk.Label(status_frame, 
        text=str(total))
    c_errors.grid(column=1, row=1, pady=6, padx=6)

def scrape_categories():
    """Scrapes categories from www.lyrics.com"""
    print("--- CATEGORY SCRAPING STARTED ---")
    print("Scraping from ::", HOME_PAGE)
    
    soup = get_soup(HOME_PAGE)
    category_links = get_links(soup, "^/artists/")
    a_tags = set(category_links)
    hrefs = get_hrefs(a_tags)
    suffixed = add_suffixes(hrefs, "/99999")
    categories = add_prefixes(suffixed, HOME_PAGE)
    save(categories, CATEGORY_FILE)
    
    successes = count_all_lines(CATEGORY_FILE)
    errors =count_all_lines(CATEGORY_ERRORS)
    
    #draw successes
    c_total.grid_forget()
    redraw_category_total(successes)

    #draw errors
    c_errors.grid_forget()
    redraw_category_errors(errors)
    print("--- CATEGORY SCRAPING FINISHED ---")

#Main
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
    command=scrape_categories) #sc.scrape
#working on this one

c_btn.grid(column=0, row=1, pady=6, padx=6)
a_btn = ttk.Button(status_frame, text="Artist", 
    command=buttontest)
a_btn.grid(column=0, row=2, pady=6, padx=6)
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

#tempfix
a_total = ttk.Label(status_frame, 
#    text=str(count_all_lines(ARTIST_FILE)))
    text="na")
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




#recover buttons
c_recover = ttk.Button(status_frame, text="recover", 
    command=buttontest)
c_recover.grid(column=3, row=1, pady=6, padx=6)
a_recover = ttk.Button(status_frame, text="recover", 
    command=buttontest)
a_recover.grid(column=3, row=2, pady=6, padx=6)
s_recover = ttk.Button(status_frame, text="recover", 
    command=buttontest)
s_recover.grid(column=3, row=3, pady=6, padx=6)
l_recover = ttk.Button(status_frame, text="recover", 
    command=buttontest)
l_recover.grid(column=3, row=4, pady=6, padx=6)

#bottom buttons
button_frame = ttk.LabelFrame(main_box)
button_frame.grid(column=0, row=2, sticky=tk.W, pady=6, padx=6)

#temp fix
run_tests_btn = ttk.Button(button_frame, text="Run Tests", 
#    command=run_test)
    command=buttontest)
run_tests_btn.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)

win.mainloop()
