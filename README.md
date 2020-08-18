# Python Web Scraper

## Approach 1
-   Decided not to use this approach
```python
    # Scrape all links for each city then scrape those links as well 
    # NOTE: Noticed this may be the wrong approach
    # Why not ? (Too much iterating and use of requests)
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

## Desired Dictionary
```python
    {
        "UNITED_STATES": {   
            "RI": {
                "Providence": [
                            {
                                    bizName: "--"
                                    address:"---",
                                    phoneNumber: "---",
                                    about: "---",
                                    imageUrl: "---"
                            },
                            {
                                    bizName: "--"
                                    address:"---",
                                    phoneNumber: "---",
                                    about: "---",
                                    imageUrl: "---"
                            },
                        ],
                }, 

            "PA": {
                "Pittsburgh": [
                            {
                                    bizName: "--"
                                    address:"---",
                                    phoneNumber: "---",
                                    about: "---",
                                    imageUrl: "---"
                            },
                            {
                                    bizName: "--"
                                    address:"---",
                                    phoneNumber: "---",
                                    about: "---",
                                    imageUrl: "---"
                            },
                        ],

                "Philidelphia": [
                            {
                                    bizName: "--"
                                    address:"---",
                                    phoneNumber: "---",
                                    about: "---",
                                    imageUrl: "---"
                            },
                            {
                                    bizName: "--"
                                    address:"---",
                                    phoneNumber: "---",
                                    about: "---",
                                    imageUrl: "---"
                            },
                        ],
                },
       
    }
```

## Where I am at now?
```python
# 8/18/20
# So far can almost create the desired dictionary,
# would just haft to parse cities from address strings to figure 
# out where it shold be in the structure so for now I can make for EX:
{
    "UNITED_STATES": {   

        "RI": [
            {
                    bizName: "--"
                    address:"---",
                    phoneNumber: "---",
                    about: "---",
                    imageUrl: "---"
            },
            {
                    bizName: "--"
                    address:"---",
                    phoneNumber: "---",
                    about: "---",
                    imageUrl: "---"
            },
        ],

        "PA": [
                {
                        bizName: "--"
                        address:"---",
                        phoneNumber: "---",
                        about: "---",
                        imageUrl: "---"
                },
                {
                        bizName: "--"
                        address:"---",
                        phoneNumber: "---",
                        about: "---",
                        imageUrl: "---"
                },
                {
                        bizName: "--"
                        address:"---",
                        phoneNumber: "---",
                        about: "---",
                        imageUrl: "---"
                },
                {
                        bizName: "--"
                        address:"---",
                        phoneNumber: "---",
                        about: "---",
                        imageUrl: "---"
                },
            ], 

    }
```