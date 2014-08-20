# -*- coding: utf-8 -*-

# Author: Danilo Scorzoni Ré
# Date: 20/08/2014

# Loading necessary packages

import urllib2
from BeautifulSoup import BeautifulSoup

# This function gets all the links in a URL, limited to a specified
# domain name.

def spider(url, closed_domain):

	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	url_list = []

	for tag in soup.findAll('a', href=True):
		full_url = tag['href'].replace('http://','').replace('https://','')
		domain = full_url.split('/')[0]
		if (domain == closed_domain):
			url_list.append(full_url)
		
	url_distinct = set(url_list)
	
	return url_distinct
	

