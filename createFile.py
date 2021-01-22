# Creates html files with a page source string.
def createFile(fileName, contents):
    with open(f"{fileName}", "w") as file:
        file.write(contents + "\n")
        file.close()