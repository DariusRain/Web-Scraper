# Attempting to do an all in one, good suggestion @GaberialSherman
import json
import requests
import time
from addressParser import stateParser
from bs4 import BeautifulSoup
from secrets import pathOfListings, pathOfErrorMessage1, pathOfErrorMessage2, pathOfListingItems, pathToBuisinessName, pathToAddress, pathToCategories, pathToPhoneNumber, pathToDescription, pathToImage, pathToWebsite
from createJsonOffline import createJsonFileOffline

#  NOTE 8/25 urlOfAllListings is no longer need now using list of urls

# This function returns a dictrionary see README for structured example.
def getListingsOffline():
    # TECHNICAL / ANALOGY
    # Get response class / Get soup ingredients
    # res = requests.get(urlOfAllListings)

    # # Parse Text / Cook the Soup!
    # soup = BeautifulSoup(res.text, 'lxml')

    # Init Dictionary / Set the table
    curPage = []
    counter = int(input("Number of data-<X> file start:"))
    datacounterEnd = int(input("counter of data-<X> file end:"))
    title = input("What would you like the new file name to start with ex: <name>-1.json:")
    # read the json that contains the links, will contain an object with a property for each person
    # dev will enter their name and the correct list will be used in scraper
    # format will be... {name: [ { link: 'http://link.com', pages: int }]} }
    while counter <= datacounterEnd:
        try:
            with open(f"offline/data-{counter}.html") as response:
                soup = BeautifulSoup(response, "lxml")
                error = soup.select(pathOfErrorMessage1)
                error2 = soup.select(pathOfErrorMessage2)
                if len(error) == 0 and len(error2) == 0:
                    for item in soup.find_all("div", pathOfListingItems):
                        buisinessName = item.find("a", pathToBuisinessName)
                        image = item.find("img", pathToImage)
                        website = item.find("a", pathToWebsite)
                        phonecounterber = item.find("a", pathToPhoneNumber)
                        description = item.find("div", pathToDescription)
                        parsedAddress = stateParser(item.find(pathToAddress).get_text())

                        newBiz = type("NewBiz", (object,), {})()
                        if not buisinessName == None:
                            newBiz.name = buisinessName.get_text().strip()

                        if not phonecounterber == None:
                            newBiz.phonecounterber = phonecounterber.get_text().strip()
                        
                        if not description == None:
                            newBiz.description = description.get_text().strip()
                        
                        if not website == None:
                            newBiz.website = website.get("href").strip()
                        
                        if not image == None:
                            newBiz.image = image["data-src"].strip()

                        if not parsedAddress == None:
                            newBiz.address = parsedAddress["address"]

                        curPage.append(json.dumps(newBiz.__dict__))    

                else:
                    continue
                # print(curPage)
                createJsonFileOffline(counter, curPage, title)
                counter += 1
        except:
            print("Skipping unreadable data")
            continue

    print("Done")
