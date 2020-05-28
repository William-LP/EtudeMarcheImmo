# Import libraries
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

code_postal = {}

for i in range(1, 23, 1):  # for i in range(0, 8, 8):
    url = "https://www.proprietes-privees.com/achat/renovation?page=" + str(i) + "&controller=Application%5CController%5CAchat&action=index&type=renovation"
    if (urllib.request.urlopen(url).getcode()) == 200:
        # print(url + " : OK")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        h4s = soup.find_all("h4", class_="offer-city-name")
        for h4 in h4s:
            cp = re.sub("[^0-9]", "", h4.text)
            if cp in code_postal:
                code_postal[cp] += 1
            else:
                code_postal[cp] = 1

for k, v in code_postal.items():
    print(k, ':', v)
