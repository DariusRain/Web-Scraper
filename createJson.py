import json
# def createJsonFile(fileName, dict):
#     with open(fileName, "w", encoding="utf8") as outfile:
#         json.dump(dict, outfile, ensure_ascii=False)
def createJsonFile(counter, data, dev, region):
    
    fileName = f"{region}-{counter}"
    with open('./region-count.json') as regionCount:
        rCount = json.load(regionCount)
    
    rCount[dev][region] = counter

    with open('./region-count.json', "w") as modRCount:
        json.dump(rCount, modRCount, ensure_ascii=False)

    with open(f"scraped/{fileName}.json", "w") as outfile:
        json.dump({ "bizs" : data }, outfile, ensure_ascii=False)

        