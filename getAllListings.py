# Attempting to do an all in one, good suggestion @GaberialSherman
import requests
from bs4 import BeautifulSoup
from secrets import urlOfAllListings, pathOfListings, rootUrl



def getListings():

    # Get response class / Get soup ingredients
    res = requests.get(urlOfAllListings)

    # Parse Text / Cook the Soup!
    soup = BeautifulSoup(res.text, 'lxml')

    # Initilize array to contain objects
    extracted = []
    
    # Find Data / Eat the soup
    for link in soup.select(pathOfListings)[0].find_all("a"):
        cityName = ''.join([i for i in link.get('href').split("/")[-1] if not i.isdigit()]).replace("-", "")
        extracted.append({"name": f"{cityName}", "link":f"{rootUrl}{link.get('href')}"})
    
    print(extracted)

