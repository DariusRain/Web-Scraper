# Libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from variables import urlOfCities

# Set the URL you want to webscrape from

# Connect to the URL
response = requests.get(urlOfCities)

soup = bs4.BeautifulSoup(response.text, 'lxml')



# Parse HTML and save to BeautifulSoup object¶
# soup = BeautifulSoup(response.text, "html.parser")

# # To download the whole data set, let's do a for loop through all a tags
# line_count = 1 # variable to track what line you are on
# for one_a_tag in soup.findAll('a'):  # 'a' tags are for links
#     if line_count >= 36: # Code for text files starts at line 36
#         link = one_a_tag['href']
#         download_url = 'http://web.mta.info/developers/'+ link
#         urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
#         time.sleep(1) # Pause the code for a sec
#     # Add 1 for next line
#     line_count +=1