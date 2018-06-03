import csv
import json
import re
from bs4 import BeautifulSoup
from datetime import *

def str_strip_tags_sc(a):
  soup  = BeautifulSoup(a,"html.parser")
  str   = soup.get_text()
  clean = re.sub('\W+','', str )
  return clean.strip()

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# csvfilename = 'data.csv'
# jsonfilename = csvfilename.split('.')[0] + '.json'
# csvfile = open(csvfilename, 'r')
# jsonfile = open(jsonfilename, 'w')
# reader = csv.DictReader(csvfile)
# fieldnames = ("by","score","time","title","type","url","text","parent")
# output = []
# for each in reader:
#   row = {}
#   for field in fieldnames:
#     row[field] = each[field]
#     output.append(row)
# a=json.dumps(output)
# print(a[1])


csvfilename = 'data.csv'
jsonfilename = csvfilename.split('.')[0] + '.json'
csvfile = open(csvfilename, 'r')
jsonfile = open(jsonfilename, 'w')
reader = csv.DictReader(csvfile)
fieldnames = ("by","score","time","title","type","url","text","parent")

output = []

for each in reader:
  row = {}
  for field in fieldnames:
    row[field] = each[field]
    output.append(row)
for i in output:
  dt=i["time"]
  try:
      dt=datetime.fromtimestamp(int(dt)).strftime("%Y-%b-%d %I:%M:%S")
  except:
      pass
  # i["time"]=dt
  i["converted timestamp"]=dt

  text=i["text"]
  text=cleanhtml(text)
  i["text"]=text

print(i)

C = 'ñ'
U = C.encode()
U
u'\xf1'

json.dump(output, jsonfile, indent=2, sort_keys=True)
