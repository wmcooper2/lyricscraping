#3rd party
import pytest

#custom
from constants import *
from scrapeutil import *

def test_simple_request():
    assert simple_request(HOME_PAGE).status_code == 200

# how to test?
#def test_three_requests()

def test_persistent_request():
    assert persistent_request(HOME_PAGE).status_code == 200

def test_get_links():
    soup = get_soup(HOME_PAGE)
    #maybe a problem with LINKSTRINGTEST later on
    assert type(get_links(soup, LINKSTRINGTEST)).__name__ == "ResultSet"

def test_get_soup():
    assert type(get_soup(HOME_PAGE)).__name__ == "BeautifulSoup"
    
#def test_save_list():

#def test_save_json():

#def test_load_json():

def test_count_unique_lines():
    assert count_unique_lines(LINECOUNTTEST) == 5

def test_count_all_lines():
    assert count_all_lines(LINECOUNTTEST) == 6

#def test_write_to_file():

def test_load_file_list():
    assert type(load_file_list(LINECOUNTTEST)) is list
    assert len(load_file_list(LINECOUNTTEST)) == 6

#def test_count_songs():

#def test_count_files():

#def test_count_files():

#def test_buttontest():
