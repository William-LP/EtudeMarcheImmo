import urllib.request

for i in range(0, 328, 8):
    url = "http://www.maison-a-renover.fr/immobilier/toutes-annonces?start=" + str(i)
    if (urllib.request.urlopen("http://www.stackoverflow.com").getcode()) == 200:
        print(url + " : OK")
