import re
import time
import string
from bs4 import BeautifulSoup
from operator import itemgetter
from urllib.request import Request, urlopen

import tomd

### SETTINGS ###
################
timeout = 500  # Timeout between Checking URLS (Milliseconds)
element = 'body' # You can search for a specific element to count words in
element_attrs = {} # Example attribute below.
# element_attrs = {
	# "class": 'my-class',
	# "id": 'my-id',
# }
################

globalcomp = False
urls = []
lines = []
with open('urls.txt') as f:
	content = f.readlines()
	lines = [x.strip() for x in content] 
# Checking for comma separation
for url in lines:
	urlObject = {}
	if ",!" in url:
		array = url.split(",")
		globalcomp = re.sub("!", "", array[1])
	if "," in url:
		array = url.split(",")
		urlObject = {
			"url": array[0],
			"comp": re.sub("!", "", array[1])
		}
	else:
		comp = 0
		if globalcomp:
			comp = globalcomp
		urlObject = {
			"url": url,
			"comp": comp
		}
	urls.append(urlObject)

def getHTML(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
	fp = urlopen(req)
	html = fp.read().decode("utf8")
	fp.close()
	return html

if __name__ == "__main__":
	for url in urls:
		html = getHTML(url['url'])
		soup = BeautifulSoup(html, 'html.parser')
		html = str(soup.find(element, attrs=element_attrs))
		html = tomd.convert(html)
		wordlist = re.sub("[^\w]", " ", html).split()
		word_count = len(wordlist)
		if not globalcomp:
			if(url.get('comp', False)):
				word_count -= int(url['comp'])
		else:
			word_count -= int(globalcomp)
		print(url['url'], ': ', word_count)
		time.sleep(float(timeout/1000))
