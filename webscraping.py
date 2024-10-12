from bs4 import BeautifulSoup
import requests
import sys
import os

def main():
    URL = "http://www.values.com/inspirational-quotes"
    # try webscraping zillow or something.
    # we have to analyze the raw html ourselves to find the locations of the area, i guess.
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    '''
    Libraries needed if you want to test this code on your home computer.
=========================================================================
    pip install requests
    pip install html5lib
    pip install bs4
=========================================================================
    '''
    print(soup.prettify())
    break

if (__name__ == "__main__"):
    main()
    sys.exit()
