import json
# def createJsonFile(fileName, dict):
#     with open(fileName, "w", encoding="utf8") as outfile:
#         json.dump(dict, outfile, ensure_ascii=False)
def createJsonFileOffline(counter, data, title):
    fileName = f"{title}-{counter}"
    with open(f"scraped/{fileName}.json", "w") as outfile:
        json.dump({ "bizs" : data }, outfile, ensure_ascii=False)