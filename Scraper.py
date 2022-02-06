from bs4 import BeautifulSoup
import requests

with open("Test.html", ("r")) as f:
	doc = BeautifulSoup(f, ("html.parser"))

