"""All of the steps combined to scrape from lyrics.com"""
#stand lib
from pathlib import Path
from urllib.parse import unquote

#custom
from constants import *
from scrapeutil import *

def count_artists():
    """Counts all artists links already scraped. Returns Integer."""
    total = 0
    for x in Path(ARTIST_DIR).iterdir():
        if str(x).endswith("txt"):
            total += count_unique_lines(str(x))
    return total

def scrape():
    """Main scraping function. Returns None."""
    print("--- ARTIST SCRAPING STARTED ---")
    errors = []
    cat_links = load_file_list(CATEGORY_FILE)
    for cat in cat_links:
        try:
            soup = get_soup(cat)
            art_hrefs = get_links(soup, "^artist")
            art_links = list(map(format_artist_link, art_hrefs))
            category = Path(cat).parts[3]
            text_file = (ARTIST_DIR+category+"_"+"artistlinks.txt") 
            save(art_links, text_file)
            print("saved", text_file)
        except:
            errors.append(cat)
            print("Error::", cat)
    save(errors, ARTIST_ERRORS)
    print("--- ARTIST SCRAPING FINISHED ---")

if __name__ == "__main__":
    scrape()
