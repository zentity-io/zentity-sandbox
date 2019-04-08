"""
PECOS Enrollment Row Structure
-------------------
0 NPI
1 PECOS_ASCT_CNTL_ID
2 ENRLMT_ID
3 PROVIDER_TYPE_CD
4 PROVIDER_TYPE_DESC
5 STATE_CD
6 FIRST_NAME
7 MDL_NAME
8 LAST_NAME
9 ORG_NAME
10 GNDR_SW
"""

import csv
import json

FILENAME_INPUT = "C:\\data\\pecos_enrollment\\Base_Provider_Enrollment_file.csv"
FILENAME_OUTPUT = "C:\\data\\pecos_enrollment\\pecos_enrollment.ndjson"

def row_to_doc(row):
    for x in xrange(len(row)):
        row[x] = row[x].strip()
        
    doc = {}
    if row[0]:
        doc["npi"] = row[0]
    if row[1]:
        doc["pecos_asct_cntl_id"] = row[1]
    if row[2]:
        doc["enrlmnt_id"] = row[2]
    if row[3]:
        doc["provider_type_cd"] = row[3]
    if row[4]:
        doc["provider_type_desc"] = row[4]
    if row[5]:
        doc["state_cd"] = row[5]
    if row[6]:
        doc["first_name"] = row[6]
    if row[7]:
        doc["mdl_name"] = row[7]
    if row[8]:
        doc["last_name"] = row[8]
    if row[9]:
        doc["org_name"] = row[9]
    if row[10]:
        doc["gndr_sw"] = row[10]
    return doc

with open(FILENAME_INPUT, "rb") as input:
    with open(FILENAME_OUTPUT, "wb") as output:
        for i, row in enumerate(csv.reader(input, delimiter=",", quotechar='"')):
            if i == 0:
                continue
            if i % 10000 == 0:
                print "{:,}".format(i)
            doc = row_to_doc(row)
            #print json.dumps(doc, indent=2, sort_keys=True)
            print >> output, json.dumps(doc, indent=None, separators=(",", ":"), sort_keys=False, ensure_ascii=False)
            