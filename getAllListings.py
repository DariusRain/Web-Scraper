# Attempting to do an all in one, good suggestion @GaberialSherman
import requests
import time
from addressParser import stateParser
from bs4 import BeautifulSoup
from secrets import urlOfAllListings, pathOfListings, pathOfErrorMessage1, pathOfErrorMessage2, pathOfListingItems, pathToBuisinessName, pathToAddress, pathToCategories, pathToPhoneNumber, pathToDescription, pathToImage, pathToWebsite
from createJson import createJsonFile

# This function returns a dictrionary see README for structured example.
def getListings():
    # TECHNICAL / ANALOGY
    # Get response class / Get soup ingredients
    # res = requests.get(urlOfAllListings)

    # # Parse Text / Cook the Soup!
    # soup = BeautifulSoup(res.text, 'lxml')

    # Init Dictionary / Set the table
    bizs = []

    # Init counter for iterations of the future / Prepare for company  
    counter = int(input("Start on page: "))
    
    pageEnd = int(input("End on page: "))

    # While TRUE loop will break from inside due to unkown amount of iterations / While people are hungry
    while(counter <= pageEnd):
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
                print(parsedAddress)
                if parsedAddress == None or buisinessName == None or phoneNumber == None or image == None:
                    continue
                buisinessName = buisinessName.get_text().strip()
                phoneNumber = phoneNumber.get_text().strip()
                description = description.get_text().strip()
                if not website == None:
                    website = website.get("href").strip()
                else:
                    website = ""
                image = image["data-src"].strip()
                state = parsedAddress["state"]
                address = parsedAddress["address"]
                bizs.append({"name": buisinessName, "state":state, "address": address, "phoneNumber": phoneNumber, "description": description, "imageUrl": image, "website": website })    
                
        else:
            if not len(error2) == 0:
                print("Server has blocked scraper")
            if not len(error) == 0:
                print("Done")
            break

        print("Sleeping...")
        createJsonFile(f"bizs-{counter}", bizs)
        time.sleep(30)
        counter += 1

    return bizs

