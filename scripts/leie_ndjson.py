"""
LEIE Row Structure
-------------------
0 LASTNAME
1 FIRSTNAME
2 MIDNAME
3 BUSNAME
4 GENERAL
5 SPECIALTY
6 UPIN
7 NPI
8 DOB
9 ADDRESS
10 CITY
11 STATE
12 ZIP
13 EXCLTYPE
14 EXCLDATE
15 REINDATE
16 WAIVERDATE
17 WVRSTATE
"""

import csv
import json

FILENAME_INPUT = "C:\\data\\leie\\UPDATED.csv"
FILENAME_OUTPUT = "C:\\data\\leie\\leie.ndjson"

def row_to_doc(row):
    for x in xrange(len(row)):
        row[x] = row[x].strip()
        
    doc = {}
    if row[0]:
        doc["lastname"] = row[0]
    if row[1]:
        doc["firstname"] = row[1]
    if row[2]:
        doc["midname"] = row[2]
    if row[3]:
        doc["busname"] = row[3]
    if row[4]:
        doc["general"] = row[4]
    if row[5]:
        doc["specialty"] = row[5]
    if row[6]:
        doc["upin"] = row[6]
    if row[7] and row[7] != "0" and row[7] != "00000000":
        doc["npi"] = row[7]
    if row[8] and row[8] != "0" and row[8] != "00000000":
        doc["dob"] = row[8]
    if row[9]:
        doc["address"] = row[9]
    if row[10]:
        doc["city"] = row[10]
    if row[11]:
        doc["state"] = row[11]
    if row[12]:
        doc["zip"] = row[12]
    if row[13]:
        doc["excltype"] = row[13]
    if row[14] and row[14] != "0" and row[14] != "00000000":
        doc["excldate"] = row[14]
    if row[15] and row[15] != "0" and row[15] != "00000000":
        doc["reindate"] = row[15]
    if row[16] and row[16] != "0" and row[16] != "00000000":
        doc["waiverdate"] = row[16]
    if row[17]:
        doc["wvrstate"] = row[17]
    return doc

with open(FILENAME_INPUT, "rb") as input:
    with open(FILENAME_OUTPUT, "wb") as output:
        for i, row in enumerate(csv.reader(input, delimiter=",", quotechar='"')):
            if i == 0:
                continue
            if i % 10000 == 0:
                print "{:,}".format(i)
            doc = row_to_doc(row)
            #print json.dumps(doc, indent=3, sort_keys=True)
            print >> output, json.dumps(doc, indent=None, separators=(",", ":"), sort_keys=False, ensure_ascii=False)
            