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
import os

data_directory = "ipeds_data"
enrolment_data = "2013_ENROLMENT_DATA.csv"
price_data = "CSV_292015-507_2013_PRICE_DATA.csv"

output_name = "college_data.json"

enrolment = open(os.path.join(data_directory, enrolment_data), "r")
price = open(os.path.join(data_directory, price_data), "r")

