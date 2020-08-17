# Attempting to do an all in one, good suggestion @GaberialSherman
import requests
import time
from bs4 import BeautifulSoup
from secrets import urlOfAllListings, pathOfListings, pathOfErrorMessage, pathOfListingItem



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

    states = {}
    counter = 0

    # Approach 1
    # Scape all links for each city then scrape those links as well
    # NOTE: Noticed this may be the wrong approach
    # # Find Data / Eat the soup
    # for link in soup.select(pathOfListings)[0].find_all("a"):
    #     cityName = ''.join([i for i in link.get('href').split("/")[-1] if not i.isdigit()]).replace("-", "")
    #     extracted.append({"name": f"{cityName}", "link":f"{rootUrl}{link.get('href')}"})
    

    # Approach 2
    # Use time's sleep method then send a request for each <url><pagination-number>
    # Then scrape data similarly scince each page should be identical until the error page
    while(True):
        response = None
        if not counter == 0:
            response = requests.get(urlOfAllListings)
            print(f"Scraping: {urlOfAllListings}")
        else:
            response = requests.get(f"{urlOfAllListings}/p:{counter}")
            print(f"Scraping: {urlOfAllListings}/p:{counter}")
        
        soup = BeautifulSoup(response.text, "lxml")
        
        if soup.select(pathOfErrorMessage) == None:
           for listing in soup.find("div", pathOfListings).find_all("div", pathOfListingItem)
        print("Sleeping...")
        time.sleep(60)
    print(extracted)

