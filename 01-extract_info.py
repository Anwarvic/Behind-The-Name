# -*- coding: utf-8 -*-

"""
The reason for this pyhton file is to extract some info from the 69 pages in this url (www.behindthename/names), the url
of the first page is written as (www.behindthename/names/1). 
These info are:
- name: the name itself
- gender: m for masculine, and f for feminine
- origin: the origin of the name like (ARABIC, ENGLISH, BIBLE, ...etc)
- meaning: the meaning of the name

Then, we put every page inside a pickle file inside 'PAGES' folder. So, the following url (www.behindthename/names/1) 
will be put as pickle file (page1.pickle).
"""

import re
import requests
import pickle
from bs4 import BeautifulSoup



def extract_info(parsed):
    """
    This function is used to extract [name, gender, origin, meaning]. It takes an HTML page and returns a list 
    of dictionaries. Each name is a dictionary, of a value of entities.
    So, the output would be like:

    """
    for i in parsed:
        name.append(i.a.get_text())
        gender.append(i.span.get_text())
        links = i.find_all('a', class_='usg')
        temp = []
        for j in links:
            temp.append(j.get_text())
        origin.append(temp)
        meaning.append(i.get_text())

for k in range(1, 70):
	name = []
	gender = []
	origin = []
	meaning = []
	file_name = "PAGES/page"+str(k)+".pickle"
	url = "http://www.behindthename.com/names/"+ str(k)
	page = requests.get(url)
	page.encoding = 'utf-8'
	soup = BeautifulSoup(page.content, 'html.parser')

	names1 = soup.find_all('div', class_='browsename b0')
	extract_info(names1)
	names2 = soup.find_all('div', class_='browsename b1')
	extract_info(names2)
	output = {	"name": name,
				"gender": gender,
				"origin": origin,
				"meaning":meaning
			 }
	print file_name
	print len(name), len(gender), len(origin), len(meaning)
	with open(file_name, "wb") as f:
		pickle.dump(output, f)
	


