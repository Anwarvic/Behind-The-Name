# -*- coding: utf-8 -*-
"""
This file extracts some information from each name in our corpus, this info is:
 - 'related' table which contains [Equivalent Names, Masculine Forms, Feminie Names, ....]
 - 'pronounciation' which explains how to pronounce the name.
 - 'scripts' which puts different script for the name, so for example the script of Mohamed is محمد

"""

import pickle
import requests
from bs4 import BeautifulSoup
from correctify import *

def get_pronounciation(text):
	"""
	This function is used to extract the 'pronounciation' field
	"""
	start = text.find("PRONOUNCED")
	end = text.find("[", start)
	if end < 0:
		end = text.find("\n", start)
	return text[start:end].strip()

def get_scripts(text):
	"""
	This function is used to extract the 'Other scripts' field
	"""
	start = text.find("OTHER SCRIPTS")
	end = text.find("\n", start)
	return text[start:end].strip()

def get_info (page):
	"""
	This function is used to call both "ger_pronounciation()" and "get_scripts()" methods
	"""
	page.encoding = 'utf-8'
	soup = BeautifulSoup(page.content, 'lxml')
	body = soup.find('div', class_= 'body') 
	info = soup.find('div', class_= 'nameinfo') 
	if info == None:
		return "", ""
	text = info.text

	if "OTHER SCRIPTS" in text:
		scripts = get_scripts(text)
	else:
		scripts =""

	if "PRONOUNCED" in text:
		pronounciation = get_pronounciation(text)
	else:
		pronounciation =""

	return pronounciation, scripts

def get_related (page):
	"""
	This function is used to get the "related" field
	"""
	page.encoding = 'utf-8'
	soup = BeautifulSoup(page.content, 'lxml')
	body = soup.find('div', class_= 'body') 
	#14348 has no body, how funcking come
	related = []
	table = body.find('table')
	if table == None:
		return related
	table_rows = table.find_all("tr")
	for tr in table_rows:
		td = tr.find_all('td')
		for i in td:
			related.append(i.text)
	return related

with open("dataset2.pickle", "r") as f:
	df = pickle.load(f)

for i in range(21):
	related = []
	pronounciation = []
	scripts = []
	if i == 20:
		last = len(df["name"])
		for index, row in df.loc[i*1000:last].iterrows():
			print index, "	", row["name"].encode("utf-8")
			name = correctify(row["name"])
			url = "http://www.behindthename.com/name/" + name +"/related"
			try: 
				page = requests.get(url)
				temp_lst = get_related (page)
				related.append(temp_lst)

			except requests.exceptions.ConnectionError:
				print False, "----------------------> Here "
				related.append([])
				
			url = "http://www.behindthename.com/name/" + name
			try: 
				page = requests.get(url)
				pronounciation.append(get_info(page)[0]) 
				scripts.append(get_info(page)[1])

			except requests.exceptions.ConnectionError:
				print False, "----------------------> Here "
				pronounciation.append([])
				scripts.append([])

	else:	
		for index, row in df.loc[i*1000:(i+1)*1000-1].iterrows():
			print index, "	", row["name"].encode("utf-8")
			name = correctify(row["name"])
			url = "http://www.behindthename.com/name/" + name +"/related"
			try: 
				page = requests.get(url)
				temp_lst = get_related (page)
				related.append(temp_lst)

			except requests.exceptions.ConnectionError:
				print False, "----------------------> Here "
				related.append([])
				
			url = "http://www.behindthename.com/name/" + name
			try: 
				page = requests.get(url)
				pronounciation.append(get_info(page)[0]) 
				scripts.append(get_info(page)[1])

			except requests.exceptions.ConnectionError:
				print False, "----------------------> Here "
				pronounciation.append("")
				scripts.append("")

	df2 = {	"related": related,
			"pronounciation": pronounciation,
			"scripts": scripts}

	print len(related), len(pronounciation), len(scripts), "\n"
	with open("MORE/"+str(i*1000)+".pickle", "wb") as f:
		pickle.dump(df2, f)
