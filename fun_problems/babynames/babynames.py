import json

file = open('names/yob1880.txt')
yearlist = []
full_list = {}

for i in file:
  babyname = {}
  row = i.strip().split(",")
  babyname['name'] = row[0]
  babyname['gender'] = row[1]
  babyname['rank'] = row[2]
  yearlist.append(babyname)

print(yearlist)
  
file.close()