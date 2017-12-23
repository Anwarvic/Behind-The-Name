# -*- coding: utf-8 -*-
import pickle
import pandas as pd

def handle_endings(text):
	endings = "._,()[]{})"
	if text[0] in endings:
		return handle_endings(text[1:])
	elif  text[-1] in endings:
		return handle_endings(text[:-1])
	else:
		return text.strip()

def get_special(special_word, lst):
	output = []
	try:
		idx = lst.index(special_word)
		for word in lst[idx+1:]:
			word = word.encode("utf-8")
			if word not in special_words and len(word)> 0:
				output.append(word)
	except ValueError:
		pass
	return output

def formalize(lst):
	output = handle_endings(str(lst[0]))+"("
	length = len(lst)
	for word in lst[1:]:
		output += handle_endings(word)
		if word != lst[length-1]:
			output += ", "
	output += ")"
	return output

def group_language(lst):
	output = []
	temp = []
	if len(lst) != 0:
		for word in lst:
			if ":" in word and len(temp)== 0:
				temp = word.split(":")
			elif ":" in word and len(temp)!= 0:
				output.append(formalize(temp))
				temp = word.split(":")
			elif word.istitle():
				temp.append(word)
		if len(temp)!= 0:
			output.append(formalize(temp))

	return output

def del_start(text):
	"""
	This function is used to deleted some extra words from the "OTHER SCRIPTS" field 
	and "PRONOUNCED" field.
	For example, "OTHER SCRIPTS: محمي (Arabic)" will be "محمي (Arabic)"
	"""
	if type(text) == unicode:
		text = text.encode("utf-8")
	if len(text) == 0:
		return ""
	lst = text.split(": ")
	return "".join(lst[1:])

def get_groups(lst):
	temp = get_special('EQUIVALENTS', lst)
	equivalents.append(group_language(temp))

	temp = get_special('DIMINUTIVES AND SHORT FORMS', lst)
	short_forms.append(group_language(temp))

	temp = get_special('FULL FORMS', lst)
	full_forms.append(group_language(temp))

	temp = get_special('OTHER FORMS', lst)
	other_forms.append(group_language(temp))

	temp = get_special('FEMININE FORMS', lst)
	feminine_forms.append(group_language(temp))

	temp = get_special('MASCULINE FORMS', lst)
	masculine_forms.append(group_language(temp))

	temp = get_special('OTHER READINGS', lst)
	other_readings.append(group_language(temp))	

with open("dataset2.pickle", "r") as f:
	df = pickle.load(f)

name = df["name"]
gender = df["gender"]
origin = df["origin"]
meaning = df["meaning"]

pronounciation = []
scripts = []

equivalents = []
short_forms = []
full_forms = []
other_forms = []
feminine_forms = []
masculine_forms = []
other_readings = []

special_words = [	'EQUIVALENTS', 'DIMINUTIVES AND SHORT FORMS', 'FULL FORMS', 'OTHER FORMS', 
					'FEMININE FORMS', 'MASCULINE FORMS', 'OTHER READINGS'	]


for i in range(21):
	file_name = "MORE/" + str(i*1000) + ".pickle"
	# print file_name
	with open(file_name, "r") as f:
		df = pickle.load(f)
	LENGTH = len(df["related"])
	for k in range(LENGTH):
		get_groups(df["related"][k])
		temp = del_start(df["pronounciation"][k])
		pronounciation.append(temp)
		temp = del_start(df["scripts"][k])
		scripts.append(temp)
	# print len(pronounciation), len(scripts)

# print len(name), len(pronounciation), len(scripts), len(equivalents), len(feminine_forms), len(masculine_forms)


d = {"name":name,
	 "gender": gender,
	 "origin": origin,
	 "meaning": meaning,
	 "equivalents": equivalents,
	 "short_forms": short_forms,
	 "full_forms": full_forms,
	 "other_forms": other_forms,
	 "feminine_forms": feminine_forms,
	 "masculine_forms": masculine_forms,
	 "other_readings": other_readings,
	 "pronounciation":pronounciation,
	 "scripts":scripts}

df = pd.DataFrame(d)
with open("dataset3.pickle", "w") as f:
		pickle.dump(df, f)
df.to_csv('dataset3.csv', encoding="utf-8-sig")

		

