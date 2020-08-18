# Python Web Scraper

## Approach 1
-   Decided not to use this approach
```python
    # Approach 1
    # Scrape all links for each city then scrape those links as well 
    # NOTE: Noticed this may be the wrong approach
    # Why not ? (Too much iterating and use of requests)
    # # Find Data / Eat the soup
    for link in soup.select(pathOfListings)[0].find_all("a"):
        cityName = ''.join([i for i in link.get('href').split("/")[-1] if not i.isdigit()]).replace("-", "")
        extracted.append({"name": f"{cityName}", "link":f"{rootUrl}{link.get('href')}"})
    

    # Approach 2
    # send a request for each <url><pagination-number> & use the time library's sleep method during the end of each iteration
    # NOTE: Each iteration represents the scraping of a single pagniated page.
    # Then scrape data similar to aproach 1 & each page should be identical until the error page
```