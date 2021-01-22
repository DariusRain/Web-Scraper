# Creates html files with a page source string.
def createHtmlFile(fileName, html):
    with open(f"{fileName}.html", "w") as file:
        file.write(html)
        file.close()