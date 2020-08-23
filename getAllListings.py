import requests
import time
from addressParser import stateParser
from bs4 import BeautifulSoup
from secrets import urlOfAllListings, pathOfListings, pathOfErrorMessage1, pathOfErrorMessage2, pathOfListingItems, pathToBuisinessName, pathToAddress, pathToCategories, pathToPhoneNumber, pathToDescription, pathToImage, pathToWebsite
from createJson import appendToJsonFile

def getListings():
    counter = int(input("Start on page: "))
    
    pageEnd = int(input("End on page: "))

    while(counter <= pageEnd):
        
        response = None
        
        if counter == 0:
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
                if parsedAddress == None or buisinessName == None or phoneNumber == None or image == None:
                    continue
                buisinessName = buisinessName.get_text().strip()
                phoneNumber = phoneNumber.get_text().strip()
                description = description.get_text().strip()
                website = website.get("href").strip()
                image = image["data-src"].strip()
                state = parsedAddress["state"]
                address = parsedAddress["address"]
                appendToJsonFile({"name": buisinessName, "state": state, "address": address, "phoneNumber": phoneNumber, "description": description, "imageUrl": image, "website": website })    
                
        else:
            if not len(error2) == 0:
                print("Server has blocked scraper")
            if not len(error) == 0:
                print("Done")
            break

        print("Sleeping...")
        time.sleep(30)
        counter += 1

