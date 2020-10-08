import json
import time
from addressParser import stateParser
from secrets import *
from createJson import createJsonFile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# import requests
# from bs4 import BeautifulSoup
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# driver.quit()
def getListings():
    
    currPage = []
    pageCount = 0
    counter = 1
    linkCount = 0
    driver.get(urlOfAllListings + str(pageCount))
    while(len(driver.find_elements(By.TAG_NAME, "div")) != 0):    
        try:  
            listing = driver.find_elements(By.CSS_SELECTOR, pathToListing)
            newBiz = type("NewBiz", (object,), {})()
            
            # Debug 
            # print(listing.text)            
            
            # print(counter, len(listing))
            for item in listing:
                try:
                    newBiz.categories = []
                    newBiz.contact = []
                    phoneNumber = item.find_element(By.CSS_SELECTOR, pathToPhoneNumber).text.replace(".", "")
                    newBiz.contact.append({ "type": "phoneNumber", "data": phoneNumber })
                    newBiz.name = item.find_element(By.CSS_SELECTOR, pathToBuisinessName).text.split(". ")[1]
                    newBiz.description = item.find_element(By.TAG_NAME, "p").text
                    categoriesList = item.find_element(By.CSS_SELECTOR, pathToCategories).find_elements(By.TAG_NAME, "a")
                    
                    for category in categoriesList:
                        newBiz.categories.append(category.text)
                    
                    contactList = item.find_element(By.CSS_SELECTOR, pathToContact).find_elements(By.TAG_NAME, "a")

                    for contactType in contactList:
                        propName = contactType.get_attribute("title").lower()
                        if not propName == "":
                            linkTo = contactType.get_attribute("href").replace("mailto:", "")
                            newBiz.contact.append({ "type":  propName, "data": linkTo}) 
                    
                    newBiz.address = item.find_element(By.CSS_SELECTOR, pathToAddress).text

                except NoSuchElementException:
                    print("Had an issue getting feild")
                    
                
                finally:
                    currPage.append(json.dumps(newBiz.__dict__))   
                    print("currPage length:", len(currPage))
        finally:
            
            # Debug
            # print("name:", newBiz.name)
            # print("address:", newBiz.address)
            # print("description:", newBiz.description)
            # print("categories:", newBiz.categories)
            # print("contact:", newBiz.contact)
            # print("\n\nSleeping...")

            createJsonFile(counter, currPage)
            time.sleep(3)
            pageCount += 10
            counter += 1
            currPage.clear()
            driver.get(urlOfAllListings + str(pageCount))
    driver.quit()
   

























# Scrape 2
# #  NOTE 8/25 urlOfAllListings is no longer need now using list of urls

# # This function returns a dictrionary see README for structured example.
# def getListings():
#     curPage = []
#     response = None
#     # response = requests.get(urlOfAllListings)      
#     soup = BeautifulSoup(html_doc1, "lxml")
    
#     print(f"Scraping: {urlOfAllListings}")
    
#     # For each item 
#     for item in soup.find_all("div", pathOfListingItems):
#         buisinessName = item.select(pathToBuisinessName)
#         image = item.select(pathToImage)
#         address = item.select(pathToAddress)
#         newBiz = type("NewBiz", (object,), {})()


#         urlOfExtraItem = urlBase + item.find("a", pathToExtraItem)["href"]
#         print(f"Scraping: {urlOfExtraItem}")
#         response2 = requests.get(urlOfExtraItem)
#         soup2 = BeautifulSoup(response2.text, "lxml")
#         print(soup2.find_all("div", {"class": "kn-label-top kn-table is-unbordered"}))
#         description = soup2.select(pathToDescription)
#         phoneNumber = soup2.select(pathToPhoneNumber)
#         website = soup2.select(pathToWebsite)
#         email = soup2.select(pathToEmail)
#         links = soup2.find_all("a")
#         # if not len(buisinessName) == 0:
#         print("BuisinessName", buisinessName)
#         #     newBiz.name = buisinessName[0].get_text().strip()

#         # if not len(phoneNumber) == 0:
#         print("PhoneNumber", phoneNumber)
#         #     newBiz.phoneNumber = phoneNumber[0].get_text().strip()
        
#         # if not len(description) == 0:
#         print("Description", description)
#         #     newBiz.description = description[0].get_text().strip()
        
#         # if not len(website) == 0:
#         print("Website", website)
#         #     newBiz.website = website[0]
        
#         # if not len(image) == 0:
#         print("Image", image)
#         #     newBiz.image = image[0].strip()

#         # if not len(address) == None:
#         print("Address", address)
#         #     newBiz.address = stateParser(address[0])["address"]
#         print("Email", email)

#         print("Links", links)
#         # curPage.append(json.dumps(newBiz.__dict__))    
            
#     print("Done...")




    # createJsonFile(1, curPage)

    # return curPage


    # Scrape 1
    # import json
    # import requests
    # import time
    # from addressParser import stateParser
    # from bs4 import BeautifulSoup
    # from secrets import pathOfListings, 
    # pathOfErrorMessage1, 
    # pathOfErrorMessage2, 
    # pathOfListingItems, 
    # pathToBuisinessName,
    # pathToAddress, 
    # pathToCategories, 
    # pathToImage, 
    # # On seprate page
    # pathToExtraItem
    # pathToDescription, 
    # pathToPhoneNumber,
    # pathToWebsite,
    # pathToEmail,

    # from createJson import createJsonFile
    # TECHNICAL / ANALOGY
    # Get response class / Get soup ingredients
    # res = requests.get(urlOfAllListings)

    # # Parse Text / Cook the Soup!
    # soup = BeautifulSoup(res.text, 'lxml')

    # Init Dictionary / Set the table
    # curPage = []

    # read the json that contains the links, will contain an object with a property for each person
    # dev will enter their name and the correct list will be used in scraper
    # format will be... {name: [ { link: 'http://link.com', pages: int }]} }
    # with open('./links.json') as linksList:
    #     allLinks = json.load(linksList)

    # with open('./region-count.json') as countList:
    #     allCounts = json.load(countList)

    # dev = str(input("Enter Name: "))

    # if dev in allLinks:
    #     print(f"Your In {dev}!")
    # else:
    #     return print(f"The Name '{dev}' Can Not Be Used")
    # # Init counter for iterations of the future / Prepare for company  
    # personalLinks = allLinks[dev]
    
    # for region in personalLinks:
    #     # gets the page to scrape from the list of links one at a time
    #     base = region['link']
    #     # start with page 1 because excluding the number from the link is the same as using pagination, 
    #     # gets the maximum number of pages for a state in the same object as the link
    #     pageEnd = region['pages']
    #     # simply the name of the region
    #     rName = region['name']
        
    #     # if set to 0 it will grab page one twice and get a duplicate file
    #     counter = None
    #     if rName in allCounts[dev]:
    #         counter = allCounts[dev][rName]+1
    #     else: 
    #         counter = 1
    # While TRUE loop will break from inside due to unkown amount of iterations / While people are hungry
    # def getListings():

    #     while(counter <= pageEnd):
    #         # Initial value to None to prevent operations on a NoneType value / Prepare for no visitors at all
    #         response = None

    #         response = requests.get(urlOfListings)
            
    #         soup = BeautifulSoup(response.text, "lxml")
    #         error = soup.select(pathOfErrorMessage1)
    #         error2 = soup.select(pathOfErrorMessage2)
            
    #         if not len(error2) == 0:
    #             print("Server has blocked scraper")
    #             break;

    #         if not len(error) == 0:
    #             print("Done")
    #             break 
            
    #         print(f"Scraping: {base}/p:{counter}")
    #         for item in soup.find_all("div", pathOfListingItems):
    #             buisinessName = item.find("a", pathToBuisinessName)
    #             image = item.find("img", pathToImage)
    #             website = item.find("a", pathToWebsite)
    #             phoneNumber = item.find("a", pathToPhoneNumber)
    #             description = item.find("div", pathToDescription)
    #             parsedAddress = stateParser(item.find(pathToAddress).get_text())

    #             newBiz = type("NewBiz", (object,), {})()
    #             if not buisinessName == None:
    #                 newBiz.name = buisinessName.get_text().strip()

    #             if not phoneNumber == None:
    #                 newBiz.phoneNumber = phoneNumber.get_text().strip()
                
    #             if not description == None:
    #                 newBiz.description = description.get_text().strip()
                
    #             if not website == None:
    #                 newBiz.website = website.get("href").strip()
                
    #             if not image == None:
    #                 newBiz.image = image["data-src"].strip()

    #             if not parsedAddress == None:
    #                 newBiz.address = parsedAddress["address"]

    #             curPage.append(json.dumps(newBiz.__dict__))    
                    
    #         print("Sleeping...")
    #         createJsonFile(counter, curPage, dev, rName)
    #         time.sleep(3)
    #         counter += 1
    #         curPage = []