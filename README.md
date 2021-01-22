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

## Where I am at now?
```python
# 10/8/20
# Using Selenium to scrape
# https://www.selenium.dev

# Learned that you can use a web driver from a provider such as (Google, FireFox, Opera, etc.)
# And the webdriver's use is to mimic a client so you can unlock way more capapblities to scrape & interact with the webpage dynamically.

```