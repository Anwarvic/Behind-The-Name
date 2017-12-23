# Behind The Name

This repo contains a crawler that I have created to extract the names from [Behind the name](https://www.behindthename.com) website which has more than 20,000 names. 

The names that I have extracted have these attributes:

- **name**: This attribute  is the name itself.
- **pronounciation**: This attribute describes the pronunciation of the name. e.g. "Abraham" is pronounced as "Ab-rah-hahm".
- **origin**: This attribute describes the origin of the name. e.g. the origin of "Abraham" is [Biblical Greek, Georgian].
- **gender**: This attribute describes the gender of the name ("m" as "male", "f" as female and "m&f" as "unisex"). e.g. "Abraham" is a masculine name, thus its gender attribute is "m".
- **equivalents**: This attribute enumerates the equivalent names in other origins. e.g. "Abraham" has these equivalents:
  - ARABIC(Ebrahim, Ibraheem, Ibrahim)
  - BIBLICAL GREEK(Abraam)
  - BIBLICAL HEBREW(Avraham)
  - BIBLICAL LATIN(Abraham)
  - BIBLICAL(Abraham)
  - CHECHEN(Ibragim)
-  **scripts**: This attribute enumerates the other scripts that the name is written with. e.g. "Abraham" can be written as:
  - Αβρααμ (Ancient Greek).
  - აბრაამ (Georgian).
- **short_forms**: This attribute enumerates the other short version of the name. e.g. "Abraham" has these short versions:
  - BOSNIAN(Ibro)
  - DUTCH(Braam, Bram)
  - ENGLISH(Abe, Bram)
  - FINNISH(Aapo)
  - HEBREW(Avi)
  - LIMBURGISH(Braam)
  - BIBLICAL HEBREW(Avram)
  - BIBLICAL(Abram)
- **masculine_forms**: This attribute enumerates the masculine names of the name. e.g. "ABELONE" is a feminine name, but it has some masculine forms like:
  - ANCIENT GREEK(Apollonios)
  - GREEK MYTHOLOGY(Apollon)
- **feminine_forms**: This attribute enumerates the feminine names of the name. e.g. "AATAMI" is a masculine name, but it has some feminine forms like:
  - ENGLISH(Adamina)
  - ENGLISH(Addison, Addyson, Edison)



# My Solution

The crawler that I have created is consisted of eight files:

- 01-extract_info.py
- 02-combine_into_one_pickle.py
- 03-prune.py
- 04-expand_names.py
- 05-check_empty.py
- 05-last_cleaning.py
- 07-combine_last.py
- correctify.py



## 01-extract_info.py

This file is to extract some info from the 69 pages in the website main address which is [www.behindthename/names](www.behindthename/names). So, it gets 69 different urls', the url of the first page is written as ([www.behindthename/names/1](www.behindthename/names/1)) and the url of the last page is ([www.behindthename/names/1](www.behindthename/names/1)). 
Then, we open the url using Beautiful Soup 4 and extract these info:

- **name**: the name itself
- **gender**: m for masculine, and f for feminine
- **origin**: the origin of the name like (ARABIC, ENGLISH, BIBLE, ...etc)
- **meaning**: the meaning of the name

Then, we put every page inside a pickle file inside 'PAGES' directory. So, the following url (www.behindthename/names/1) 
will be put as pickle file (page1.pickle).



## 02-combine_into_one_pickle.py

This file is used to combine the pickle files inside 'PAGES' directory into one pickle 'dataset.pickle'

This file will be a dictionary of four lists:

- df["name"]: 20505 name
- df["gender"]: 20505 gender
- df["origin"]: 20505 origin
- df["meaning"]: 20505 meaning



## 03-prune.py

This file reads the "dataset.pickle" file and then it does basically two things:

- 'gender' entity doesn't get f&m, it shows only one of them, so we are going to add them.
- 'meaning' entity has some extra words at the beginning, we are going to get rid of them.

Finally, it saves the pruned data into a second pickle file "dataset2.pickle"



## 04-expand_names.py

This file reads the "dataset2.pickle" file and use the name parameter to construct a url name, then use that url to extract some information from the website. this info is:

 - 'related' table which contains [Equivalent Names, Masculine Forms, Feminie Names, ....]
 - 'pronounciation' which explains how to pronounce the name.
 - 'scripts' which puts different script for the name, so for example the script of Mohamed is محمد

Finally, it saves the new data into another directory called "MORE"



## 05-check_empty.py

This file reads the data from the "MORE" directory and checks if some data was empty. 



## 06-last_cleaning.py

This file is very important. It reads the "MORE" directory data and then does these things:

- Split the **related** attribute into these groups:
  - EQUIVALENTS
  - DIMINUTIVES AND SHORT FORMS'
  - 'FULL FORMS
  - OTHER FORMS
  - FEMININE FORMS
  - MASCULINE FORMS
  - OTHER READINGS
- Delete some extra words from "OTHER SCRIPTS" attribute.
- Finally, save the last form of data into a pickle file "dataset3.pickle"



## 07-combine_last.py

This file is used to read data from "PAGES" directory and "MORE" directory and combine them in two files which are "dataset3.pickle" and "dataset3.csv".



## correctify.py

This website follows a certain schema for urls that are related to a certain name. e.g. the url of "Abraham" is "https://www.behindthename.com/name/abraham". And this is very good, but what about the names that contain unicode characters like "Ábrahám". 

This file deals with such a problem.