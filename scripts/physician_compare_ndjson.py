"""
Physician Compare Row Structure
-------------------
0 NPI
1 Ind_PAC_ID
2 Ind_enrl_ID
3 lst_nm
4 frst_nm
5 mid_nm
6 suff
7 gndr
8 Cred
9 Med_sch
10 Grd_yr
11 pri_spec
12 sec_spec_1
13 sec_spec_2
14 sec_spec_3
15 sec_spec_4
16 sec_spec_all
17 org_nm
18 org_pac_id
19 num_org_mem
20 adr_ln_1
21 adr_ln_2
22 ln_2_sprs
23 cty
24 st
25 zip
26 phn_numbr
27 hosp_afl_1
28 hosp_afl_lbn_1
29 hosp_afl_2
30 hosp_afl_lbn_2
31 hosp_afl_3
32 hosp_afl_lbn_3
33 hosp_afl_4
34 hosp_afl_lbn_4
35 hosp_afl_5
36 hosp_afl_lbn_5
37 assgn
38 PQRS
39 EHR
40 MHI
"""

import csv
import json

FILENAME_INPUT = "C:\\data\\physician_compare\\Physician_Compare_National_Downloadable_File.csv"
FILENAME_OUTPUT = "C:\\data\\physician_compare\\physician_compare.ndjson"

def row_to_doc(row):
    for x in xrange(len(row)):
        row[x] = row[x].strip()
        
    doc = {}
    if row[0]:
        doc["npi"] = row[0]
    if row[1]:
        doc["ind_pac_id"] = row[1]
    if row[2]:
        doc["ind_enrl_id"] = row[2]
    if row[3]:
        doc["lst_nm"] = row[3]
    if row[4]:
        doc["frst_nm"] = row[4]
    if row[5]:
        doc["mid_nm"] = row[5]
    if row[6]:
        doc["suff"] = row[6]
    if row[7]:
        doc["gndr"] = row[7]
    if row[8]:
        doc["cred"] = row[8]
    if row[9]:
        doc["med_sch"] = row[9]
    if row[10]:
        doc["grd_yr"] = row[10]
    if row[11]:
        doc["pri_spec"] = row[11]
    doc["sec_spec"] = []
    if row[12]:
        doc["sec_spec"].append(row[12])
    if row[13]:
        doc["sec_spec"].append(row[13])
    if row[14]:
        doc["sec_spec"].append(row[14])
    if row[15]:
        doc["sec_spec"].append(row[15])
    if not doc["sec_spec"]:
        del doc["sec_spec"]
    if row[17]:
        doc["org_nm"] = row[17]
    if row[18]:
        doc["org_pac_id"] = row[18]
    if row[19]:
        doc["num_org_mem"] = int(row[19])
    if row[20]:
        doc["adr_ln_1"] = row[20]
    if row[21]:
        doc["adr_ln_2"] = row[21]
    if row[22]:
        if row[22] == "Y":
            doc["ln_2_sprs"] = True
        if row[22] == "N":
            doc["ln_2_sprs"] = False
        else:
            doc["ln_2_sprs"] = None
    if row[23]:
        doc["cty"] = row[23]
    if row[24]:
        doc["st"] = row[24]
    if row[25]:
        doc["zip"] = row[25]
    if row[26]:
        doc["phn_numbr"] = row[26]
    doc["hosp_afl"] = []
    hosp = {}
    if row[27]:
        hosp["ccn"] = row[27]
    if row[28]:
        hosp["lbn"] = row[28]
    if hosp:
        doc["hosp_afl"].append(hosp)
    hosp = {}
    if row[29]:
        hosp["ccn"] = row[29]
    if row[30]:
        hosp["lbn"] = row[30]
    if hosp:
        doc["hosp_afl"].append(hosp)
    hosp = {}
    if row[31]:
        hosp["ccn"] = row[31]
    if row[32]:
        hosp["lbn"] = row[32]
    if hosp:
        doc["hosp_afl"].append(hosp)
    hosp = {}
    if row[33]:
        hosp["ccn"] = row[33]
    if row[34]:
        hosp["lbn"] = row[34]
    if hosp:
        doc["hosp_afl"].append(hosp)
    hosp = {}
    if row[35]:
        hosp["ccn"] = row[35]
    if row[36]:
        hosp["lbn"] = row[36]
    if hosp:
        doc["hosp_afl"].append(hosp)
    if not doc["hosp_afl"]:
        del doc["hosp_afl"]
    if row[37]:
        if row[37] == "Y":
            doc["assgn"] = True
        if row[37] == "N":
            doc["assgn"] = False
        else:
            doc["assgn"] = None
    if row[38]:
        if row[38] == "Y":
            doc["pqrs"] = True
        if row[38] == "N":
            doc["pqrs"] = False
        else:
            doc["pqrs"] = None
    if row[39]:
        if row[39] == "Y":
            doc["ehr"] = True
        if row[39] == "N":
            doc["ehr"] = False
        else:
            doc["ehr"] = None
    if row[40]:
        if row[40] == "Y":
            doc["mhi"] = True
        if row[40] == "N":
            doc["mhi"] = False
        else:
            doc["mhi"] = None
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
            