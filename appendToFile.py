# Appends to file by name of file and what to append
def appendFile(fileName, content):
    with open(fileName, "a") as file:
        file.write(content + "\n")
        file.close()

