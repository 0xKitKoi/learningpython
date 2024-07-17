import re

def Main():
    line = "I think I understand regular expressions."
    matchResult = re.match('think', line, re.M|re.I) # no match found because it didnt match the whole string
    if matchResult:
        print("Match found: " + matchResult.group())
    else:
        print("No Match was found.")

    searchResult = re.search('think', line, re.M|re.I) # think is found because its inside the string
    if searchResult:
        print("Search Found: " + searchResult.group())
    else:
        print("Nothing Found in search")

if __name__ == '__main__':
    Main()
