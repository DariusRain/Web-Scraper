# Libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from secrets import urlOfCities, rootUrl


# Connect to the URL
def getCityLinks():
    
    res = requests.get(urlOfCities)

    soup = BeautifulSoup(res.text, 'lxml')

    linksEl = soup.find(attrs={"banner-type": "skyscraper"}).next_element.next_element.find_all("a")

    extractedLinks = []

    for link in linksEl: 
        cityName = ''.join([i for i in link.get('href').split("/")[-1] if not i.isdigit()]).replace('-',  "").capitalize()
        extractedLinks.append({f"{cityName}": f"{rootUrl}{link.get('href')}"})
        
    # DEBUG:
    # print(extractedLinks)
