# Import libraries
import requests
from bs4 import BeautifulSoup
import urllib.request

code_postal = {}

for i in range(0, 328, 8):  # for i in range(0, 8, 8):
    url = "http://www.maison-a-renover.fr/immobilier/toutes-annonces?start=" + str(i)
    if (urllib.request.urlopen(url).getcode()) == 200:
        # print(url + " : OK")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        spans = soup.find_all("div", class_="mid94")
        for span in spans:
            cp = span.find("span", {"class": "lkdv"}).text
            if cp in code_postal:
                code_postal[cp] += 1
            else:
                code_postal[cp] = 1

for k, v in code_postal.items():
    print(k, ':', v)
