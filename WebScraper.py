from bs4 import BeautifulSoup
import requests
import time

url = "https://www.newegg.com/asus-geforce-rtx-3080-ti-rog-strix-rtx3080ti-o12g-gaming/p/N82E16814126508"

while(True):
	header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
	}
	result = requests.get(url, headers = header)
	doc = BeautifulSoup(result.text, "html.parser")
	prices = doc.find_all(text = "$")
	parent = prices[0].parent
	strong = doc.find_all("strong")
	sup = doc.sup
	price = " $ " + strong[1].string + sup.string
	txt = strong[1].string
	x = txt.split(",")
	y = x[0]+x[1]
	y = int(y)

	if (y >= 2000):
		print(price + "   Don't Buy")
	elif(y <= 500):
		print(price + "   Buy Now")
	else:
		print(price)
	time.sleep(100)


