import requests
import time
from bs4 import BeautifulSoup

def scrapeListings(listings):
    for listing in listings:
        