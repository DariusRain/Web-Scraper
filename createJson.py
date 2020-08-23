import json
# def createJsonFile(fileName, dict):
#     with open(fileName, "w", encoding="utf8") as outfile:
#         json.dump(dict, outfile, ensure_ascii=False)
def createJsonFile(fileName, bizs):
    with open(f"scraped/{fileName}.json", "w") as outfile:
        json.dump({ "bizs" : bizs }, outfile, ensure_ascii=False)

        