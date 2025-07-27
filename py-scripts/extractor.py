import json
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# Create a nested defaultdict that defaults to dict
surname_json = defaultdict(dict)
total_surname_count = 0

def getURL(alpha):
    if alpha < 'e':
        year, month = '1999', '10'
    elif alpha == 'e' or alpha == 'g':
        year, month = '2014', '07'
    else:
        year, month = '2000', '07'
    return f"http://greatkamma.blogspot.in/{year}/{month}/kamma-gothrams-surname-alphabet-{alpha}.html"

def splitandAdd(arr, gothrams):
    for mergedGothrams in arr:
        for gothram in mergedGothrams.split(','):
            if gothram:
                gothrams.append(gothram)

    return gothrams

def getRestSurnames():
    for i in range(97, 123):
        global total_surname_count
        alpha = chr(i)
        if alpha == 'g':
            continue
        print(f"Fetching surnames starting with {alpha}...", end="")
        response = requests.get(getURL(alpha))
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        surname_count = 0

        for row in rows:
            cols = row.text.split()
            if len(cols) < 2 or 'Gothram' in cols:
                continue

            surname = cols[1]
            gothrams = []

            if len(cols) > 2:
                gothrams = splitandAdd(cols[2::], gothrams)

            surname_json[alpha.upper()][surname] = gothrams
            surname_count += 1
        print(f" Done - found {surname_count} surnames.")
        total_surname_count += surname_count

def getGSurnames():
    global total_surname_count
    print(f"Fetching surnames starting with g...", end="")
    sepURL = "https://kammapeople.blogspot.com/2016/02/initial-names-with-g-respective-gotrams.html"
    response = requests.get(sepURL)
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('span', attrs={'class': None})
    surname_count = 0

    for row in rows[2:-2]:
        cols  = row.text.split()
        try:
            if int(cols[0]):
                surname = cols[1]
                gothrams = []
                gothrams = splitandAdd(cols[2::], gothrams)
                surname_count = surname_count + 1
        except:
            gothrams = splitandAdd(cols, gothrams)

        surname_json['G'][surname] = gothrams
    print(f" Done - found {surname_count} surnames.")
    total_surname_count += surname_count

print("Starting the fetch:")
getGSurnames()
getRestSurnames()
print(f"Data Fetched Successfully. Found a total of {total_surname_count} surnames. Below is the output:")
print(surname_json)

file_name = 'surnameData.json'
with open(file_name, 'w') as f:
    json.dump(surname_json, f)
    print(f"Wrote the JSON into {file_name}")
