from bs4 import BeautifulSoup
import requests

with open("The name of the file", ("r")) as f:
	doc = BeautifulSoup(f, ("html.parser"))

