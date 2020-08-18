# Attempting to do an all in one, good suggestion @GaberialSherman
import requests
import time
from addressParser import stateParser
from bs4 import BeautifulSoup
from secrets import urlOfAllListings, pathOfListings, pathOfErrorMessage, pathOfListingItems, pathToBuisinessName, pathToAddress, pathToCategories, pathToPhoneNumber, pathToDescription, pathToImage, pathToWebsite



def getListings():

    # Get response class / Get soup ingredients
    res = requests.get(urlOfAllListings)

    # Parse Text / Cook the Soup!
    soup = BeautifulSoup(res.text, 'lxml')

    # Initilize dicitonary to contain:
    # Attempting to format in the following structure 
    #   {   
    #      "RI": {
    #           "Providence": {
    #                   "biz name": {
    #                         address:"---",
    #                         phoneNumber: "---",
    #                         about: "---",
    #                         imageUrl: "---"
    #                       },
    #               },
    #    }, 

    extracted = {}
    counter = 0

    while(counter == 0):
        response = None
        if counter == 0:
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
                image = item.select(pathToImage)
                website = item.find("a", pathToWebsite)
                phoneNumber = item.find("a", pathToPhoneNumber)
                description = item.find("div", pathToDescription)
                # category = item.find("div", pathToCategories).find_all("a")
                parsedAddress = stateParser(item.find(pathToAddress).get_text())
                # print({"name": buisinessName, "phoneNumber": phoneNumber, "description": description, "imageUrl": image, "website": website })
                if parsedAddress == None or buisinessName == None or phoneNumber == None:
                        print("Skipping buisiness w/ out required values...")
                        continue
                buisinessName = buisinessName.get_text().strip()
                phoneNumber = phoneNumber.get_text().strip()
                description = description.get_text().strip()
                website = website.get("href").strip()
                print(image)
                # category = category[0].get_text().strip()
                state = parsedAddress["state"]
                address = parsedAddress["address"]
                if state not in extracted:
                    extracted[state] = []
                    print(extracted)
                extracted[state].append({"name": buisinessName,  "address": address, "phoneNumber": phoneNumber, "description": description, "imageUrl": image, "website": website })    
        else:
            print("Done")
            break

        print("Sleeping...")
        time.sleep(20)
        counter += 1
        
    print(extracted)

