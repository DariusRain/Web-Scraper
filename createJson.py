import json
# def createJsonFile(fileName, dict):
#     with open(fileName, "w", encoding="utf8") as outfile:
#         json.dump(dict, outfile, ensure_ascii=False)
def initializeJsonFile():
    with open("all.json", "w") as outfile:
        json.dump([], outfile, ensure_ascii=False)

def appendToJsonFile(newBizObj):
    with open("all.json", "r+") as jsonFile:
        current = json.load(jsonFile)
        current.append(newBizObj)
        json.dump(current, jsonFile)
        