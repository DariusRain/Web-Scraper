import json
def createJsonFile(unitedStatesDict):
    with open("data.json", "w", encoding="utf8")  as outfile:
        json.dump(unitedStatesDict, outfile)