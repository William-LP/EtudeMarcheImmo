# Import libraries
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import datetime

# http://www.maison-a-renover.fr/immobilier/toutes-annonces?start=1
# https://www.proprietes-privees.com/achat/renovation?page=1&controller=Application%5CController%5CAchat&action=index&type=renovation
# https://www.superimmo.com/achat/maison/ile-de-france,rhone-alpes,provence-alpes-cote-d-azur,nord-pas-de-calais,pays-de-la-loire,bretagne,midi-pyrenees,centre,lorraine,languedoc-roussillon,picardie,haute-normandie,alsace,poitou-charentes,bourgogne,basse-normandie,champagne-ardenne,auvergne,franche-comte,limousin,corse/a-renover/p/1

maison_a_renover_max = 320
maison_a_renover_pas = 8
proprietes_privees_max = 22
proprietes_privees_pas = 1
superimmo_max = 1384
superimmo_pas = 1

now = datetime.datetime.now()
print("Starting time : " + now.strftime("%Y-%m-%d %H:%M:%S"))

code_postal = {}
print("\n")
print("SCRAPPING : ")
for i in range(0, maison_a_renover_max + maison_a_renover_pas, maison_a_renover_pas):
    print('maison-a-renover.fr' + ' [%d%%]\r' % (i * 100 / maison_a_renover_max), end="")
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

for i in range(1, proprietes_privees_max, proprietes_privees_pas):  # for i in range(0, 8, 8):
    print('proprietes-privees.com' + ' [%d%%]\r' % (i * 100 / proprietes_privees_max), end="")
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


for i in range(1, superimmo_max, superimmo_pas):
    print('superimmo.com - [%d%%]\r' % (i * 100 / superimmo_max), end="")
    url = "https://www.superimmo.com/achat/maison/ile-de-france,rhone-alpes,provence-alpes-cote-d-azur,nord-pas-de-calais,pays-de-la-loire,bretagne,midi-pyrenees,centre,lorraine,languedoc-roussillon,picardie,haute-normandie,alsace,poitou-charentes,bourgogne,basse-normandie,champagne-ardenne,auvergne,franche-comte,limousin,corse/a-renover/p/" + \
        str(i)
    if (urllib.request.urlopen(url).getcode()) == 200:
        # print(url + " : OK")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        bs = soup.find_all("b")
        for b in bs:
            reg = re.search(r'^([A-Z][a-z]+[ ]\([0-9]{5}\))$', b.text)
            if reg:
                cp = re.sub("[^0-9]", "", reg.group(0))
                # print(cp)
                if cp in code_postal:
                    code_postal[cp] += 1
                else:
                    code_postal[cp] = 1

for k, v in code_postal.items():
    print(k, ':', v)


now = datetime.datetime.now()
print("Ending time : " + now.strftime("%Y-%m-%d %H:%M:%S"))
