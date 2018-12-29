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
import scrapeutil as su

#Main
win = tk.Tk()
win.title("Webscraping Lyrics")

main_box = ttk.Frame(win)
main_box.grid(column=0, row=0, pady=6, padx=6)

address_frame = ttk.LabelFrame(main_box, text="Target", width=L_WIDTH)
address_frame.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)
address = ttk.Label(address_frame, text=HOME_PAGE)
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
c_btn = ttk.Button(status_frame, text="Categories", command=sc.scrape_everything)
c_btn.grid(column=0, row=1, pady=6, padx=6)
a_btn = ttk.Button(status_frame, text="Artists", command=sa.scrape_everything)
a_btn.grid(column=0, row=2, pady=6, padx=6)
s_btn = ttk.Button(status_frame, text="Songs", command=ss.scrape_everything)
s_btn.grid(column=0, row=3, pady=6, padx=6)
l_btn = ttk.Button(status_frame, text="Lyrics", command=sl.scrape_everything)
l_btn.grid(column=0, row=4, pady=6, padx=6)

#errors column
c_errors = ttk.Label(status_frame, text=str(su.lines_in_file(CATEGORY_ERRORS)))
c_errors.grid(column=1, row=1, pady=6, padx=6)
a_errors = ttk.Label(status_frame, text=str(su.lines_in_file(ARTIST_ERRORS)))
a_errors.grid(column=1, row=2, pady=6, padx=6)
s_errors = ttk.Label(status_frame, text=str(su.lines_in_file(SONG_ERRORS)))
s_errors.grid(column=1, row=3, pady=6, padx=6)
l_errors = ttk.Label(status_frame, text=str(su.lines_in_file(LYRIC_ERRORS)))
l_errors.grid(column=1, row=4, pady=6, padx=6)

#totals column
c_total = ttk.Label(status_frame, text=str(su.lines_in_file(CATEGORY_FILE)))
c_total.grid(column=2, row=1, pady=6, padx=6)
a_total = ttk.Label(status_frame, text=str(su.lines_in_file(ARTIST_FILE)))
a_total.grid(column=2, row=2, pady=6, padx=6)
s_total = ttk.Label(status_frame, text=str(su.count_songs2()))
s_total.grid(column=2, row=3, pady=6, padx=6)
l_total = ttk.Label(status_frame, text=str(su.count_lyrics()))
l_total.grid(column=2, row=4, pady=6, padx=6)

#recover buttons
c_recover = ttk.Button(status_frame, text="recover", command=su.button_test)
c_recover.grid(column=3, row=1, pady=6, padx=6)
a_recover = ttk.Button(status_frame, text="recover", command=su.button_test)
a_recover.grid(column=3, row=2, pady=6, padx=6)
s_recover = ttk.Button(status_frame, text="recover", command=su.button_test)
s_recover.grid(column=3, row=3, pady=6, padx=6)
l_recover = ttk.Button(status_frame, text="recover", command=su.button_test)
l_recover.grid(column=3, row=4, pady=6, padx=6)


button_frame = ttk.LabelFrame(main_box)
button_frame.grid(column=0, row=2, sticky=tk.W, pady=6, padx=6)
run_tests_btn = ttk.Button(button_frame, text="Run Tests", command=su.run_test)
run_tests_btn.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)






win.mainloop()




