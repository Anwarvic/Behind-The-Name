# -*- coding: utf-8 -*-

import re
import pickle
import pandas as pd

name = []
gender = []
origin = []
meaning = []

for k in range(1,64):
	file_name = "pages/page"+str(k)+".pickle"
	with open(file_name, "r") as f:
		container = pickle.load(f)

	for i in container:
		name.append(i["name"])
		gender.append(i["gender"])
		origin.append(i["origin"])
		meaning.append(i["meaning"])
	del container


related = []
pronounciation = []
scripts = []

for i in range(19):
	with open("RELATED/"+str(i*1000)+".pickle", "r") as f:
		df = pickle.load(f)
	related.append(df["related"])
	with open("MORE/"+str(i*1000)+".pickle", "r") as f:
		df = pickle.load(f)
	pronounciation.append(df["pronounciation"])
	scripts.append(df["scripts"])

related = sum(related,[])
pronounciation = sum(pronounciation,[])
scripts = sum(scripts,[])

d = {"name":name,
	 "gender": gender,
	 "origin": origin,
	 "meaning": meaning,
	 "related":related,
	 "pronounciation":pronounciation,
	 "scripts":scripts}

df = pd.DataFrame(d)
with open("dataset3.pickle", "w") as f:
		pickle.dump(df, f)
df.to_csv('dataset3.csv', encoding="utf-8-sig")

print len(name), len(gender), len(origin), len(meaning), len(related), len(pronounciation), len(scripts)




