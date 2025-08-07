import requests
from bs4 import BeautifulSoup

try: 
    gethtml = requests.get('https://www.ndtv.com/india#pfrom=home-ndtv_mainnavigation', )
    gethtml.raise_for_status()
    bslib = BeautifulSoup(gethtml.text, 'html.parser')

    list1 = []

    header = bslib.find_all('h2')

    i = 1
    for h in header:
        a = h.find('a')
        if a and a.text.strip():
            news = f'{i}> ' + a.text.strip() + '\n'
            list1.append(news)
        i += 1

    with open("News.txt", "w") as file:
        file.write("Today's Top News: \n\n")

    for line in list1:
        with open("News.txt", "a") as file:
            file.write(line)

    with open("News.txt", "r") as file:
        print(file.read())

except requests.exceptions.HTTPError as error: 
    print(f"\nError: {error}")