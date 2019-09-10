"""
NPPES Row Structure
-------------------
0	npi
1	entity_type_code
2	npi_replacement
3	ein
4	provider_organization_name_legal
5	provider_person_legal_name_last
6	provider_person_legal_name_first
7	provider_person_legal_name_middle
8	provider_person_legal_name_prefix
9	provider_person_legal_name_suffix
10	provider_person_legal_name_credential
11	provider_organization_name_other
12	provider_organization_name_type
13	provider_person_other_name_last
14	provider_person_other_name_first
15	provider_person_other_name_middle
16	provider_person_other_name_prefix
17	provider_person_other_name_suffix
18	provider_person_other_name_credential
19	provider_person_other_name_last_type
20	provider_business_mailing_address_line_1
21	provider_business_mailing_address_line_2
22	provider_business_mailing_address_city
23	provider_business_mailing_address_state_code
24	provider_business_mailing_address_postal_code
25	provider_business_mailing_address_country_code
26	provider_business_mailing_address_phone
27	provider_business_mailing_address_fax
28	provider_business_practice_address_line_1
29	provider_business_practice_address_line_2
30	provider_business_practice_address_city
31	provider_business_practice_address_state_code
32	provider_business_practice_address_postal_code
33	provider_business_practice_address_country_code
34	provider_business_practice_address_phone
35	provider_business_practice_address_fax
36	provider_enumeration_date
37	last_update_date
38	npi_deactivation_reason_code
39	npi_deactivation_date
40	npi_reactivation_date
41	provider_person_legal_gender
42	authorized_official_name_last
43	authorized_official_name_first
44	authorized_official_name_middle
45	authorized_official_name_title
46	authorized_official_phone
47	provider_taxonomy_code_1
48	provider_license_number_1
49	provider_license_number_state_code_1
50	provider_primary_taxonomy_switch_1
51	provider_taxonomy_code_2
52	provider_license_number_2
53	provider_license_number_state_code_2
54	provider_primary_taxonomy_switch_2
55	provider_taxonomy_code_3
56	provider_license_number_3
57	provider_license_number_state_code_3
58	provider_primary_taxonomy_switch_3
59	provider_taxonomy_code_4
60	provider_license_number_4
61	provider_license_number_state_code_4
62	provider_primary_taxonomy_switch_4
63	provider_taxonomy_code_5
64	provider_license_number_5
65	provider_license_number_state_code_5
66	provider_primary_taxonomy_switch_5
67	provider_taxonomy_code_6
68	provider_license_number_6
69	provider_license_number_state_code_6
70	provider_primary_taxonomy_switch_6
71	provider_taxonomy_code_7
72	provider_license_number_7
73	provider_license_number_state_code_7
74	provider_primary_taxonomy_switch_7
75	provider_taxonomy_code_8
76	provider_license_number_8
77	provider_license_number_state_code_8
78	provider_primary_taxonomy_switch_8
79	provider_taxonomy_code_9
80	provider_license_number_9
81	provider_license_number_state_code_9
82	provider_primary_taxonomy_switch_9
83	provider_taxonomy_code_10
84	provider_license_number_10
85	provider_license_number_state_code_10
86	provider_primary_taxonomy_switch_10
87	provider_taxonomy_code_11
88	provider_license_number_11
89	provider_license_number_state_code_11
90	provider_primary_taxonomy_switch_11
91	provider_taxonomy_code_12
92	provider_license_number_12
93	provider_license_number_state_code_12
94	provider_primary_taxonomy_switch_12
95	provider_taxonomy_code_13
96	provider_license_number_13
97	provider_license_number_state_code_13
98	provider_primary_taxonomy_switch_13
99	provider_taxonomy_code_14
100	provider_license_number_14
101	provider_license_number_state_code_14
102	provider_primary_taxonomy_switch_14
103	provider_taxonomy_code_15
104	provider_license_number_15
105	provider_license_number_state_code_15
106	provider_primary_taxonomy_switch_15
107	provider_other_id_1
108	provider_other_type_1
109	provider_other_state_code_1
110	provider_other_issuer_1
111	provider_other_id_2
112	provider_other_type_2
113	provider_other_state_code_2
114	provider_other_issuer_2
115	provider_other_id_3
116	provider_other_type_3
117	provider_other_state_code_3
118	provider_other_issuer_3
119	provider_other_id_4
120	provider_other_type_4
121	provider_other_state_code_4
122	provider_other_issuer_4
123	provider_other_id_5
124	provider_other_type_5
125	provider_other_state_code_5
126	provider_other_issuer_5
127	provider_other_id_6
128	provider_other_type_6
129	provider_other_state_code_6
130	provider_other_issuer_6
131	provider_other_id_7
132	provider_other_type_7
133	provider_other_state_code_7
134	provider_other_issuer_7
135	provider_other_id_8
136	provider_other_type_8
137	provider_other_state_code_8
138	provider_other_issuer_8
139	provider_other_id_9
140	provider_other_type_9
141	provider_other_state_code_9
142	provider_other_issuer_9
143	provider_other_id_10
144	provider_other_type_10
145	provider_other_state_code_10
146	provider_other_issuer_10
147	provider_other_id_11
148	provider_other_type_11
149	provider_other_state_code_11
150	provider_other_issuer_11
151	provider_other_id_12
152	provider_other_type_12
153	provider_other_state_code_12
154	provider_other_issuer_12
155	provider_other_id_13
156	provider_other_type_13
157	provider_other_state_code_13
158	provider_other_issuer_13
159	provider_other_id_14
160	provider_other_type_14
161	provider_other_state_code_14
162	provider_other_issuer_14
163	provider_other_id_15
164	provider_other_type_15
165	provider_other_state_code_15
166	provider_other_issuer_15
167	provider_other_id_16
168	provider_other_type_16
169	provider_other_state_code_16
170	provider_other_issuer_16
171	provider_other_id_17
172	provider_other_type_17
173	provider_other_state_code_17
174	provider_other_issuer_17
175	provider_other_id_18
176	provider_other_type_18
177	provider_other_state_code_18
178	provider_other_issuer_18
179	provider_other_id_19
180	provider_other_type_19
181	provider_other_state_code_19
182	provider_other_issuer_19
183	provider_other_id_20
184	provider_other_type_20
185	provider_other_state_code_20
186	provider_other_issuer_20
187	provider_other_id_21
188	provider_other_type_21
189	provider_other_state_code_21
190	provider_other_issuer_21
191	provider_other_id_22
192	provider_other_type_22
193	provider_other_state_code_22
194	provider_other_issuer_22
195	provider_other_id_23
196	provider_other_type_23
197	provider_other_state_code_23
198	provider_other_issuer_23
199	provider_other_id_24
200	provider_other_type_24
201	provider_other_state_code_24
202	provider_other_issuer_24
203	provider_other_id_25
204	provider_other_type_25
205	provider_other_state_code_25
206	provider_other_issuer_25
207	provider_other_id_26
208	provider_other_type_26
209	provider_other_state_code_26
210	provider_other_issuer_26
211	provider_other_id_27
212	provider_other_type_27
213	provider_other_state_code_27
214	provider_other_issuer_27
215	provider_other_id_28
216	provider_other_type_28
217	provider_other_state_code_28
218	provider_other_issuer_28
219	provider_other_id_29
220	provider_other_type_29
221	provider_other_state_code_29
222	provider_other_issuer_29
223	provider_other_id_30
224	provider_other_type_30
225	provider_other_state_code_30
226	provider_other_issuer_30
227	provider_other_id_31
228	provider_other_type_31
229	provider_other_state_code_31
230	provider_other_issuer_31
231	provider_other_id_32
232	provider_other_type_32
233	provider_other_state_code_32
234	provider_other_issuer_32
235	provider_other_id_33
236	provider_other_type_33
237	provider_other_state_code_33
238	provider_other_issuer_33
239	provider_other_id_34
240	provider_other_type_34
241	provider_other_state_code_34
242	provider_other_issuer_34
243	provider_other_id_35
244	provider_other_type_35
245	provider_other_state_code_35
246	provider_other_issuer_35
247	provider_other_id_36
248	provider_other_type_36
249	provider_other_state_code_36
250	provider_other_issuer_36
251	provider_other_id_37
252	provider_other_type_37
253	provider_other_state_code_37
254	provider_other_issuer_37
255	provider_other_id_38
256	provider_other_type_38
257	provider_other_state_code_38
258	provider_other_issuer_38
259	provider_other_id_39
260	provider_other_type_39
261	provider_other_state_code_39
262	provider_other_issuer_39
263	provider_other_id_40
264	provider_other_type_40
265	provider_other_state_code_40
266	provider_other_issuer_40
267	provider_other_id_41
268	provider_other_type_41
269	provider_other_state_code_41
270	provider_other_issuer_41
271	provider_other_id_42
272	provider_other_type_42
273	provider_other_state_code_42
274	provider_other_issuer_42
275	provider_other_id_43
276	provider_other_type_43
277	provider_other_state_code_43
278	provider_other_issuer_43
279	provider_other_id_44
280	provider_other_type_44
281	provider_other_state_code_44
282	provider_other_issuer_44
283	provider_other_id_45
284	provider_other_type_45
285	provider_other_state_code_45
286	provider_other_issuer_45
287	provider_other_id_46
288	provider_other_type_46
289	provider_other_state_code_46
290	provider_other_issuer_46
291	provider_other_id_47
292	provider_other_type_47
293	provider_other_state_code_47
294	provider_other_issuer_47
295	provider_other_id_48
296	provider_other_type_48
297	provider_other_state_code_48
298	provider_other_issuer_48
299	provider_other_id_49
300	provider_other_type_49
301	provider_other_state_code_49
302	provider_other_issuer_49
303	provider_other_id_50
304	provider_other_type_50
305	provider_other_state_code_50
306	provider_other_issuer_50
307	is_sole_proprietor
308	is_organization_subpart
309	parent_organization_lbn
310	parent_organization_tin
311	authorized_official_name_prefix
312	authorized_official_name_suffix
313	authorized_official_name_credential
314	provider_taxonomy_group_1
315	provider_taxonomy_group_2
316	provider_taxonomy_group_3
317	provider_taxonomy_group_4
318	provider_taxonomy_group_5
319	provider_taxonomy_group_6
320	provider_taxonomy_group_7
321	provider_taxonomy_group_8
322	provider_taxonomy_group_9
323	provider_taxonomy_group_10
324	provider_taxonomy_group_11
325	provider_taxonomy_group_12
326	provider_taxonomy_group_13
327	provider_taxonomy_group_14
328	provider_taxonomy_group_15
"""

import csv
import json

FILENAME_INPUT = "C:\\data\\nppes\\npidata_pfile_20050523-20190811.csv"
FILENAME_OUTPUT = "C:\\data\\nppes\\nppes.ndjson"

def row_to_doc(row):
    doc = {}
    
    # NPI
    if row[0]:
        doc["number"] = row[0]
    if row[1]:
        doc["enumeration_type_code"] = row[1]
        if doc["enumeration_type_code"] == "1":
            doc["enumeration_type"] = "individual"
        if doc["enumeration_type_code"] == "1":
            doc["enumeration_type"] = "organization"
            
    # Basic
    doc["basic"] = {}
    if row[2]:
        doc["basic"]["replacement_npi"] = row[2]
    if row[3] and row[3] != "<UNAVAIL>":
        doc["basic"]["ein"] = row[3]
    if row[36]:
        doc["basic"]["enumeration_date"] = row[36]
    if row[39]:
        doc["basic"]["deactivation_date"] = row[39]
    if row[38]:
        doc["basic"]["deactivation_reason_code"] = row[38]
    if row[40]:
        doc["basic"]["reactivation_date"] = row[40]
    if row[37]:
        doc["basic"]["last_updated"] = row[37]
    if row[4]:
        doc["basic"]["organization_name"] = row[4]
    if row[41]:
        doc["basic"]["gender"] = row[41]
    if row[5]:
        doc["basic"]["last_name"] = row[5]
    if row[6]:
        doc["basic"]["first_name"] = row[6]
    if row[7]:
        doc["basic"]["middle_name"] = row[7]
    if row[8]:
        doc["basic"]["name_prefix"] = row[8]
    if row[9]:
        doc["basic"]["name_suffix"] = row[9]
    if row[10]:
        doc["basic"]["credential"] = row[10]
    if row[42]:
        doc["basic"]["authorized_official_last_name"] = row[42]
    if row[43]:
        doc["basic"]["authorized_official_first_name"] = row[43]
    if row[44]:
        doc["basic"]["authorized_official_middle_name"] = row[44]
    if row[45]:
        doc["basic"]["authorized_official_title_or_position"] = row[45]
    if row[311]:
        doc["basic"]["authorized_official_name_prefix"] = row[311]
    if row[312]:
        doc["basic"]["authorized_official_name_suffix"] = row[312]
    if row[313]:
        doc["basic"]["authorized_official_credential"] = row[313]
    if row[46]:
        doc["basic"]["authorized_official_telephone_number"] = row[46]
    if row[307]:
        if row[307] == "Y":
            doc["basic"]["sole_proprietor"] = True
        elif row[307] == "N":
            doc["basic"]["sole_proprietor"] = True
        else:
            doc["basic"]["sole_proprietor"] = None
    if row[308] == "Y":
        doc["basic"]["organizational_subpart"] = True
    elif row[308] == "N":
        doc["basic"]["organizational_subpart"] = False
    else:
        doc["basic"]["organizational_subpart"] = None
    if row[309]:
        doc["basic"]["parent_organization_legal_business_name"] = row[309]
    if row[310] and row[310] != "<UNAVAIL>":
        doc["basic"]["parent_organization_ein"] = row[310]
    if not doc["basic"]:
        del doc["basic"]
        
    # Other Names
    doc["other_names"] = {}
    if row[11]:
        doc["other_names"]["organization_name"] = row[11]
    if row[12]:
        doc["other_names"]["code"] = row[12]
        """
        # TODO: "type" is a duplicate field
        if row[12] == "1":
            doc["other_names"]["type"] = "former"
        elif row[12] == "2":
            doc["other_names"]["type"] = "professional"
        elif row[12] == "3":
            doc["other_names"]["type"] = "dba"
        elif row[12] == "4":
            doc["other_names"]["type"] = "former_lbn"
        elif row[12] == "5":
            doc["other_names"]["type"] = "other"
            """
    if row[13]:
        doc["other_names"]["last_name"] = row[13]
    if row[14]:
        doc["other_names"]["first_name"] = row[14]
    if row[15]:
        doc["other_names"]["middle_name"] = row[15]
    if row[16]:
        doc["other_names"]["name_prefix"] = row[16]
    if row[17]:
        doc["other_names"]["name_suffix"] = row[17]
    if row[18]:
        doc["other_names"]["credential"] = row[18]
    if row[19]:
        doc["other_names"]["type"] = row[19]
    if not doc["other_names"]:
        del doc["other_names"]
        
    # Addresses
    doc["addresses"] = {}
    
    # Addresses - Mailing
    doc["addresses"]["mailing"] = {}
    if row[20]:
        doc["addresses"]["mailing"]["address_1"] = row[20]
    if row[21]:
        doc["addresses"]["mailing"]["address_2"] = row[21]
    if row[22]:
        doc["addresses"]["mailing"]["city"] = row[22]
    if row[23]:
        doc["addresses"]["mailing"]["state"] = row[23]
    if row[24]:
        doc["addresses"]["mailing"]["postal_code"] = row[24]
    if row[25]:
        doc["addresses"]["mailing"]["country_code"] = row[25]
    if row[26]:
        doc["addresses"]["mailing"]["telephone_number"] = row[26]
    if row[27]:
        doc["addresses"]["mailing"]["fax_number"] = row[27]
    if not doc["addresses"]["mailing"]:
        del doc["addresses"]["mailing"]
        
    # Addresses - Location
    doc["addresses"]["location"] = {}
    if row[28]:
        doc["addresses"]["location"]["address_1"] = row[28]
    if row[29]:
        doc["addresses"]["location"]["address_2"] = row[29]
    if row[30]:
        doc["addresses"]["location"]["city"] = row[30]
    if row[31]:
        doc["addresses"]["location"]["state"] = row[31]
    if row[32]:
        doc["addresses"]["location"]["postal_code"] = row[32]
    if row[33]:
        doc["addresses"]["location"]["country_code"] = row[33]
    if row[34]:
        doc["addresses"]["location"]["telephone_number"] = row[34]
    if row[35]:
        doc["addresses"]["location"]["fax_number"] = row[35]
    if not doc["addresses"]["location"]:
        del doc["addresses"]["location"]
    if not doc["addresses"]:
        del doc["addresses"]
        
    # Taxonomies
    doc["taxonomies"] = []
    for x in xrange(0, 15):
        start = 47
        offset = x * 4
        taxonomy = {}
        if row[start + offset + 0]:
            taxonomy["code"] = row[start + offset + 0]
        if row[start + offset + 1]:
            taxonomy["license"] = row[start + offset + 1]
        if row[start + offset + 2]:
            taxonomy["state"] = row[ start + offset + 2]
        if row[start + offset + 3]:
            if row[start + offset + 3] == "Y":
                taxonomy["primary"] = True
            elif row[start + offset + 3] == "N":
                taxonomy["primary"] = False
            else:
                taxonomy["primary"] = None
        if row[314 + x]:
            taxonomy["group_code"] = row[314 + x]
            if row[314 + x] == "193200000X":
                taxonomy["group"] = "single"
            elif row[314 + x] == "193400000X":
                taxonomy["group"] = "multiple"
        if taxonomy:
            doc["taxonomies"].append(taxonomy)
    if not doc["taxonomies"]:
        del doc["taxonomies"]
        
    # Identifiers
    doc["identifiers"] = []
    for x in xrange(0, 50):
        start = 107
        offset = x * 4
        identifier = {}
        if row[start + offset + 0]:
            identifier["identifier"] = row[start + offset + 0]
        if row[start + offset + 1]:
            identifier["code"] = row[start + offset + 1]
            if row[start + offset + 1] == "01":
                identifier["desc"] = "Other"
            elif row[start + offset + 1] == "02":
                identifier["desc"] = "MEDICARE UPIN"
            elif row[start + offset + 1] == "04":
                identifier["desc"] = "MEDICARE ID-TYPE UNSPECIFIED"
            elif row[start + offset + 1] == "05":
                identifier["desc"] = "MEDICAID"
            elif row[start + offset + 1] == "06":
                identifier["desc"] = "MEDICARE OSCAR/CERTIFICATION"
            elif row[start + offset + 1] == "07":
                identifier["desc"] = "MEDICARE NSC"
            elif row[start + offset + 1] == "08":
                identifier["desc"] = "MEDICARE PIN"
        if row[start + offset + 2]:
            identifier["state"] = row[start + offset + 2]
        if row[start + offset + 3]:
            identifier["issuer"] = row[start + offset + 3]
        if identifier:
            doc["identifiers"].append(identifier)
    if not doc["identifiers"]:
        del doc["identifiers"]
    return doc

with open(FILENAME_INPUT, "rb") as input:
    with open(FILENAME_OUTPUT, "wb") as output:
        for i, row in enumerate(csv.reader(input, delimiter=",", quotechar='"')):
            if i == 0:
                continue
            if i % 10000 == 0:
                print "{:,}".format(i)
            doc = row_to_doc(row)
            ##print json.dumps(doc, indent=3, sort_keys=True)
            print >> output, json.dumps(doc, indent=None, separators=(",", ":"), sort_keys=False, ensure_ascii=False)
            