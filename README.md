# Lyric Scraping
Scrapes lyrics from 'www.lyrics.com'

### Operation
(not finished)
_The times taken to complete a stage as shown below are when the program is running on a macbook air. This machine limits the stress on the network by restricting webpage requests to the speed at which it can process which is about one link per second, roughly. So far, this has been the easy way to reduce (almost eliminate) errors due to overloading my home router._

* Scraping is done in 4 stages;
  * category
  * artist
  * song
  * lyric
* Click on the stage buttons starting from the top when using the GUI.
* Or, run manually with 
  * `python3 webscrapergui.py` from `<programroot>/src/`
  * or `run` from `<programroot>/`

### Steps

1. Click "Category" button
  * may take 20 seconds
2. Click "Artist" button
  * may take 3 minutes
3. Click "Song" button
  * may take 40 hours
4. Click "Lyric" button
  * may take 4 months

### Notes
* You may notice that the sum of the song errors and song total don't equal the "Artist" stage total.
* This is because duplicates may exist during the "Song" scraping stage, but those clear out after the stage is finished.

### Known Bugs
* To get an updated count in the GUI, force the application closed and restart.
