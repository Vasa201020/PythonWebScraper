from bs4 import BeautifulSoup
import requests
import time

url = "https://www.zara.com/rs/en/rib-knit-top-p08779155.html?v1=166133616&v2=2026572"

while(True):
	header = {
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS 12 12_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2171.95 Safari/537.36',
	}
	result = requests.get(url, headers = header)
	doc = BeautifulSoup(result.text, "html.parser")
	tag = doc.find_all("span")
	print(tag[110].string)
	time.sleep(10)
