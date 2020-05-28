# Import libraries
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

code_postal = {}

for i in range(1, 1385, 1):
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
                print(cp)
                if cp in code_postal:
                    code_postal[cp] += 1
                else:
                    code_postal[cp] = 1

for k, v in code_postal.items():
    print(k, ':', v)
