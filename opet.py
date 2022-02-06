from bs4 import BeautifulSoup
import time
import requests

url = "https://www.zara.com/rs/en/long-coat-with-buttons-p05070151.html?v1=144946664&v2=2024686"
while(True):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS 12 12_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    result = requests.get(url, headers = header)
    doc = BeautifulSoup(result.text, "html.parser")
    tag = doc.find_all("span")
    print(tag[110].string)
    time.sleep(100)
    