"""
This file is used to do basically two things:
- 'gender' entity doesn't get f&m, it shows only one of them, so we are going to add them.
- 'meaning' entity has some extra words at the beginning, we are going to get rid of them.
"""
import pickle
import pandas as pd


def get_gender(row):
	"""
	this function is used to extract the gender from the "meaning" column
	it takes a row out of the data frame, and returns the gender as string:
	f --> female
	m --> male
	m&f --> male and female
	"""
	df_list = row["meaning"].split(" ")
	name_len = len(row["name"])
	
	if "&" in row["meaning"]:
		return "m&f"
	else:
		df_list = row["meaning"][name_len:].split()
		return df_list[0]


def prune_meaning(row):
	"""
	This function is used to remove some extra words out of the "meaning" column. It takes a row out 
	of the data frame and returns a string.
	"""
	key = row["origin"][-1]
	idx = row["meaning"].find(key)
	return row["meaning"][idx+len(key):]


with open("dataset.pickle", "r") as f:
	df = pickle.load(f)
df = pd.DataFrame(df)
for index, row in df.iterrows():
	row["gender"] = get_gender(row)
	row["meaning"] = prune_meaning(row)


df.to_csv('dataset2.csv', encoding="utf-8-sig")
with open("dataset2.pickle", "wb") as f:
     pickle.dump(df, f)   
	


