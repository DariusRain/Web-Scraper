# Attempting to do an all in one, good suggestion @GaberialSherman
import json
import requests
import time
from addressParser import stateParser
from bs4 import BeautifulSoup
from secrets import pathOfListings, pathOfErrorMessage1, pathOfErrorMessage2, pathOfListingItems, pathToBuisinessName, pathToAddress, pathToCategories, pathToPhoneNumber, pathToDescription, pathToImage, pathToWebsite
from createJson import createJsonFile

#  NOTE 8/25 urlOfAllListings is no longer need now using list of urls

# This function returns a dictrionary see README for structured example.
def getListings():
    # TECHNICAL / ANALOGY
    # Get response class / Get soup ingredients
    # res = requests.get(urlOfAllListings)

    # # Parse Text / Cook the Soup!
    # soup = BeautifulSoup(res.text, 'lxml')

    # Init Dictionary / Set the table
    curPage = []

    # read the json that contains the links, will contain an object with a property for each person
    # dev will enter their name and the correct list will be used in scraper
    # format will be... {name: [ { link: 'http://link.com', pages: int }]} }
    with open('./links.json') as linksList:
        allLinks = json.load(linksList)

    dev = str(input("Enter Name: "))

    if dev in allLinks:
        print(f"Your In {dev}!")
    else:
        return print(f"The Name '{dev}' Can Not Be Used")
    # Init counter for iterations of the future / Prepare for company  
    personalLinks = allLinks[dev]
    
    for region in personalLinks:
        # gets the page to scrape from the list of links one at a time
        base = region['link']
        # start with page 1 because excluding the number from the link is the same as using pagination, 
        # if set to 0 it will grab page one twice and get a duplicate file
        counter = 1
        # gets the maximum number of pages for a state in the same object as the link
        pageEnd = region['pages']
        # simply the name of the region
        name = region['name']
        

        # While TRUE loop will break from inside due to unkown amount of iterations / While people are hungry
        while(counter <= pageEnd):
            # Initial value to None to prevent operations on a NoneType value / Prepare for no visitors at all
            response = None

            response = requests.get(f"{base}/p:{counter}")
            print(f"Scraping: {base}/p:{counter}")
            
            
            soup = BeautifulSoup(response.text, "lxml")
            error = soup.select(pathOfErrorMessage1)
            error2 = soup.select(pathOfErrorMessage2)
            if len(error) == 0 and len(error2) == 0:
                for item in soup.find_all("div", pathOfListingItems):
                    buisinessName = item.find("a", pathToBuisinessName)
                    image = item.find("img", pathToImage)
                    website = item.find("a", pathToWebsite)
                    phoneNumber = item.find("a", pathToPhoneNumber)
                    description = item.find("div", pathToDescription)
                    parsedAddress = stateParser(item.find(pathToAddress).get_text())

                    newBiz = type("NewBiz", (object,), {})()
                    if not buisinessName == None:
                        newBiz.name = buisinessName.get_text().strip()

                    if not phoneNumber == None:
                        newBiz.phoneNumber = phoneNumber.get_text().strip()
                    
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
                if not len(error2) == 0:
                    print("Server has blocked scraper")
                if not len(error) == 0:
                    print("Done")
                break 
            # print(curPage)
            print("Sleeping...")
            createJsonFile(f"{name}-{counter}", curPage)
            time.sleep(3)
            counter += 1
            curPage = []

    # return curPage

