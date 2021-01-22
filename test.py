# Test for scraping dynamically loaded data.

import json
import time
from addressParser import stateParser
from createHtml import createHtmlFile
from secrets import *
from createJson import createJsonFile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secrets import urlOfAllListings, pathToListings

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get(urlOfAllListings)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, pathToListings)) 
)

createHtmlFile("test-1", driver.page_source)