from bs4 import BeautifulSoup

with open("The name of the file", ("r")) as f:
	doc = BeautifulSoup(f, ("html.parser"))

