# -*- coding: utf-8 -*-
import pickle 

ascii_dict = {	" ":"00", 				"-": "01",				"'":"02",				"Á":"A10",
				"À":"A11",				"Ä":"A12",				"Â":"A13",				"Ã":"A14",
				"Å":"A17",				"Ą":"A19",				"Ă":"A21",				"Ā":"A23",
				"Ả":"A27",				"Ầ":"A61",				"Æ":"AE32",				"Ǣ":"AE90",
				"Ć":"C10",				"Ĉ":"C13",				"Ç":"C15",				"Č":"C18",
				"Ð":"TH30",				"É":"E10",				"È":"E11",				"Ë":"E12",
				"Ê":"E13",				"Ě":"E18",				"Ę":"E19",				"Ė":"E20",
				"Ē":"E23",				"Ế":"E60",				"Ệ":"E62",				"Ğ":"G21",
				"Í":"I10",				"Ì":"I11",				"Ï":"I12",				"Î":"I13",
				"Ī":"I23",				"Ị":"I26",				"İ":"I50",				"Ļ":"L15",
				"Ł":"L16",				"Ñ":"N14",				"Ņ":"N15",				"Ň":"N18",
				"Ó":"O10",				"Ò":"O11",				"Ö":"O12",				"Ô":"O13",
				"Õ":"O14",				"Ø":"O16",				"Ő":"O24",				"Ơ":"O28",
				"Ồ":"O61",				"Ờ":"O64",				"Þ":"TH31",				"Ř":"R18",
				"Ś":"S10",				"Ş":"S15",				"Š":"S18",				"Ș":"S25",
				"Ț":"T25",				"Ť":"T18",				"Ú":"U10",				"Ù":"U11",
				"Ü":"U12",				"Ũ":"U14",				"Ū":"U23",				"Ư":"U28",
				"Ữ":"U67",				"Ý":"Y10",				"Ž":"Z18",				"Ż":"Z20"   }

def correctify(text):
	"""
	This function is used to change unicode string into ascii string depending on some
	certain coversion to Unicode characters.
	So, u"ÁBRAHÁM" will be "A10BRAHA10M" because "Á" is converted to "A10"
	"""
	text = text.strip()
	output = ""
	if type(text) == str:
		text = text.decode("utf-8")

	key = 0
	if "(" in text:
		lst = text.split()
		text = lst[0]
		key = 1

	for ch in text:
		try:
			ch = ch.encode("utf-8")
		except UnicodeDecodeError:
			pass
		if ch in ascii_dict.keys():
			output += ascii_dict[ch]
		else:
			output += ch
	if key:
		return (output+"-"+lst[1][1])
	return output

# TEST = u"ÁBRAHÁM"
# print correctify(TEST)
