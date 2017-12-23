# -*- coding: utf-8 -*-
import pickle


with open("dataset2.pickle", "r") as f:
	df = pickle.load(f)
names = df["name"]

def num_empty(lst):
	output = 0
	idx=0
	for i in lst:
		if len(i)==0:
			output += 1
			print idx, "	", names[idx+0]
		idx += 1
	return output


file_name = "MORE/" + str(0) + ".pickle"
with open(file_name, "r") as f:
	df = pickle.load(f)

print len(df["related"])
print num_empty(df["related"])




	


