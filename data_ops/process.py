#!python3
'''
Script to collect data from the custom dataset offered by ipeds at
http://nces.ed.gov/ipeds/datacenter/CDSPreview.aspx

The script will load all data into a json which can then be returned by
the webserver

Author: Ian Leaman

losing fundra
'''
import csv
import json
import os

# ####################### START CONSTANTS ######################
data_directory = "ipeds_data"
enrolment_data = "2013_ENROLMENT_DATA.csv"
# Enrolment file mapping:
INST_NAME = 1
STUDENT_LEVEL = 3
GRAND_TOTAL = 4
MEN_TOTAL = 5
WOMEN_TOTAL = 6

price_data = "CSV_292015-507_2013_PRICE_DATA.csv"
# Price file mapping
INST_NAME = 1
TUITION_AND_FEES = 3
IN_STATE_TOTAL = 4
OUT_STATE_TOTAL = 5

output_name = "college_data.json"
# ####################### END CONSTANTS #######################


enrolment = os.path.join(data_directory, enrolment_data)
price = os.path.join(data_directory, price_data)

normalized_data = {}
# Insert enrolment into dictionary
with open(enrolment, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[STUDENT_LEVEL] == "All students total":
            key = row[INST_NAME]
            payload = {
                "total_men_pop": row[MEN_TOTAL],
                "total_women_pop": row[WOMEN_TOTAL],
                "total_pop": row[GRAND_TOTAL],
            }

            if key in normalized_data:
                normalized_data[key].update(payload)
            else:
                normalized_data[key] = payload

with open(price, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        key = row[INST_NAME]
        payload = {
            "in_state_total": row[IN_STATE_TOTAL],
            "out_state_total": row[OUT_STATE_TOTAL],
            "tuition_and_fees": row[TUITION_AND_FEES],
        }

        if key in normalized_data:
            normalized_data[key].update(payload)
        else:
            normalized_data[key] = payload

with open(os.path.join(data_directory, output_name), "w") as fp:
    json.dump(normalized_data, fp)
