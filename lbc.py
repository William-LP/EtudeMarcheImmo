import os
import requests
from bs4 import BeautifulSoup


class lbcRequest:
    def __init__(self, ville, surface_min, piece_min, prix_max):
        self.ville = ville
        self.surface_min = surface_min
        self.piece_min = piece_min
        self.prix_max = prix_max

        self.forgedUrl = ('https://www.leboncoin.fr/recherche/?category=9&text=%C3%A0%20renover&locations=' + self.ville +
                          '&search_in=subject&immo_sell_type=old&real_estate_type=1,2&price=min-' + self.prix_max + '&rooms=' + self.piece_min + '-max&square=' + self.surface_min + '-max')


url = lbcRequest("Vichy", "70", "4", "200000").forgedUrl

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
sections = soup.find_all("section", class_="_2EDA9")
for section in sections:
    print(section)
