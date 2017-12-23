# -*- coding: utf-8 -*-

"""
This file is used to combine the pickle files incide 'PAGES' folder into one pickle 'dataset.pickle'

This file will be a dictionary of four lists:
df["name"]: 20505 name
df["gender"]: 20505 gender
df["origin"]: 20505 origin
df["meaning"]: 20505 meaning
"""
import pickle 
import pandas as pd


name = []
origin = []
gender = []
meaning = []
for k in range(1, 70):
    file_name = "PAGES/page"+str(k)+".pickle"
    print file_name
    with open(file_name, "r") as f:
		df = pickle.load(f)

    name.append(df["name"])
    gender.append(df["gender"])
    origin.append(df["origin"])
    meaning.append(df["meaning"])

output = {	"name": sum(name, []),
			"gender": sum(gender, []),
			"origin": sum(origin, []),
			"meaning":sum(meaning,[])
	    }
df = pd.DataFrame(output)

with open("dataset.pickle", "wb") as f:
    pickle.dump(output, f)
df.to_csv('dataset.csv', encoding="utf-8-sig")



