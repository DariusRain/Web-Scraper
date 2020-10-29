# Python Web Scraper

## Approach 1
-   Decided not to use this approach
```python
    # Scrape all links for each city then scrape those links as well 
    # NOTE: Noticed this may be the wrong approach
    # Why not ? (Too much iterating and use of requests)
    # Use BeutifulSoup
    # # Find Data / Eat the soup
    for link in soup.select(pathOfListings)[0].find_all("a"):
        cityName = ''.join([i for i in link.get('href').split("/")[-1] if not i.isdigit()]).replace("-", "")
        extracted.append({"name": f"{cityName}", "link":f"{rootUrl}{link.get('href')}"})
    

```
## Approach 2
```python
    # send a request for each <url><pagination-number> & use the time library's sleep method during the end of each iteration
    # NOTE: Each iteration represents the scraping of a single pagniated page.
    # Then scrape data similar to aproach 1 & each page should be identical until the error page
```
## Approach 3
```python
# Make use of the Selenium library
# pip install selenium
# Download Google Chrome (If you didnt)
# Download Google Webdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

# NOTE: In secrets.py the DRIVER_PATH is the path to the installed chromedriver
from secrets import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Enables the scrape without the browser GUI and within a server type enviroment or even any computer with GUI capabilities.
# Without the 4 lines below your chrome browser GUI would open up and display the scrape
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# Example of what I would do next
# See: https://www.selenium.dev/documentation/en/webdriver/web_element/
driver.get("< WEBSITE_URL >")
driver.find_element(By.CSS_SELECTOR, "< COPY_CSS_SELECTOR_OF_EL_IN_DEV_TOOLS >")
print(driver.text)
```

## Approach 4
```python
from secrets import *
from createJson import createJsonFile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#   This method alows the use of waiting until the element you are looking for apears in 
#  the source before further code gets executed.
from selenium.webdriver.support.ui import WebDriverWait

# This is passed as an argument to the above method for example -> 
# WebDriver( <DRIVER_VARIABLE>, <TIME-TO-WAIT> ).until( ( EC.visibility_of_element_located(By.<PATH_TYPE>, <PATH_TO_DYNAMIC_EL>) ) )
from selenium.webdriver.support import expected_conditions as EC

from appendToFile import appendFile


```
## Where I am at now?
```python
# 10/16/20
# Using Selenium to scrape still, but need to make use of the element.click() method for pagination
# https://www.selenium.dev

# 1st step is getting all the links of for each item, the link contains more details about the item
# Once all links are obtained and put in a txt file then scrape each of them for the desired data

```