from bs4 import BeautifulSoup
import requests
import time
import re



def Scraper():
	url = "https://www.zara.com/rs/en/rib-knit-top-p08779155.html?v1=166133616&v2=2026572"
	header = {
		'User-Agent': 'Mozilla/98.0 (Macintosh; Intel Mac OS 12 12_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2171.95 Safari/537.36',
	}
	result = requests.get(url, headers = header)
	doc = BeautifulSoup(result.text, "html.parser")
	tag = doc.find_all("a")
	niz = []
	konacni = []
	for x in range(len(tag)):
		try:
			niz = str(tag[x]).split("\"")
			for z in range(len(niz)):
				if (re.search("http", niz[z])):
					konacni.append(niz[z])
		except:
			print("I Can't Do It"),

	for y in range(len(konacni)):
		try:
			url = konacni[y]
			result = requests.get(url, headers = header)
			doc = BeautifulSoup(result.text, "html.parser")
			cena = doc.find("span", {"class": "price-current__amount"})
			naslov = doc.find("h1", {"class": "product-detail-info__header-name"})
			print(naslov.string + " " + cena.string)
		except:
			time.sleep(0.1)
			#print("ERROR CODE:  404")



