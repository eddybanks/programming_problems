import json
import glob
# create a dictionary with two lists: 1. list of males ; 2. list of females

# popular_names = {"male": [],"female": []}
popular_names = {}
names = {}
male_names = []
female_names = []
other_names = []

# access all files within the name directory and assign it to the variable, "files" as a list
files = glob.glob("names/*.txt")

for f in files:
  file = open(f)
  # read each row in file to obtain names and counts
  for l in file: 
    # create a list of elements from each row
    # strip: gets rid of extra spaces; split: split the string into a list using a delimiter
    row = l.strip().split(",")

    # if a (name, gender) tuple exist in the names dictionary, add the new count, otherwise initialize the tuple with the count
    # a (name, gender) tuple is used as the key because some names such as James could be both femine or masculine in the U.S
    if (row[0], row[1]) in names:
      names[(row[0], row[1])] += int(row[2])
    else:
      names[(row[0], row[1])] = int(row[2])


# Split the names into two separate lists for male and female
for k,v in names.items():
  if k[1] == 'M':
    male_names.append({"name": k[0], "count": v})
  else:
    female_names.append({"name": k[0], "count": v})

# Sort the lists in descending order (reverse=True) to obtain the 100 most popular names for each gender
m = sorted(male_names, key = lambda n: n["count"], reverse=True)
f = sorted(female_names, key = lambda n: n["count"], reverse=True)

# Designate the male and female names list as values to the corresponding male and female keys in the popular names dictionary
popular_names["male"] = m[:100]
popular_names["female"] = f[:100]

# Write the popularnames dictionary to a json file
with open('popularnames.json', 'w') as outfile:
  json.dump(popular_names, outfile)