from bs4 import BeautifulSoup
import requests
import time

url = "https://www.zara.com/rs/en/rib-knit-top-p08779155.html?v1=166133616&v2=2026572"


header = {
	'User-Agent': 'Mozilla/98.0 (Macintosh; Intel Mac OS 12 12_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2171.95 Safari/537.36',
}
result = requests.get(url, headers = header)
doc = BeautifulSoup(result.text, "html.parser")
cena = doc.find("span", {"class": "price-current__amount"})
naslov = doc.find("h1", {"class": "product-detail-info__header-name"})
print(naslov.string + " " + cena.string)
time.sleep(10)