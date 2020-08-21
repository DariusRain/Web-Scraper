# Attempting to do an all in one, good suggestion @GaberialSherman
import requests
import time
from addressParser import stateParser
from bs4 import BeautifulSoup
from secrets import urlOfAllListings, pathOfListings, pathOfErrorMessage, pathOfListingItems, pathToBuisinessName, pathToAddress, pathToCategories, pathToPhoneNumber, pathToDescription, pathToImage, pathToWebsite


# This function returns a dictrionary see README for structured example.
def getListings():
    # TECHNICAL / ANALOGY
    # Get response class / Get soup ingredients
    # res = requests.get(urlOfAllListings)

    # # Parse Text / Cook the Soup!
    # soup = BeautifulSoup(res.text, 'lxml')

    # Init Dictionary / Set the table
    unitedStates = {}

    # Init counter for iterations of the future / Prepare for company  
    counter = 0

    # While TRUE loop will break from inside due to unkown amount of iterations / While people are hungry
    while(counter == 0):
        # Initial value to None to prevent operations on a NoneType value / Prepare for no visitors at all
        response = None

        # If this is the first iteration & no dynamic paginated URL Required / If it is the first soup cooked
        if counter == 0:
            # Get raw HTML data / Open up for buisiness
            response = requests.get(urlOfAllListings)
            print(f"Scraping: {urlOfAllListings}")
        else:
            response = requests.get(f"{urlOfAllListings}/p:{counter}")
            print(f"Scraping: {urlOfAllListings}/p:{counter}")
        
        
        soup = BeautifulSoup(response.text, "lxml")
        error = soup.select(pathOfErrorMessage)
        if len(error) == 0:
           for item in soup.find_all("div", pathOfListingItems):
                buisinessName = item.find("a", pathToBuisinessName)
                image = item.find("img", pathToImage)
                website = item.find("a", pathToWebsite)
                phoneNumber = item.find("a", pathToPhoneNumber)
                description = item.find("div", pathToDescription)
                parsedAddress = stateParser(item.find(pathToAddress).get_text())
                if parsedAddress == None or buisinessName == None or phoneNumber == None or image == None:
                    continue
                buisinessName = buisinessName.get_text().strip()
                phoneNumber = phoneNumber.get_text().strip()
                description = description.get_text().strip()
                website = website.get("href").strip()
                image = image["data-src"].strip()
                state = parsedAddress["state"]
                address = parsedAddress["address"]
                if state not in unitedStates:
                    unitedStates[state] = []
                    print(f"New state added: {state}")
                unitedStates[state].append({"name": buisinessName,  "address": address, "phoneNumber": phoneNumber, "description": description, "imageUrl": image, "website": website })    
        else:
            print("Done")
            break

        print("Sleeping...")
        time.sleep(20)
        counter += 1
        
    print(unitedStates)

