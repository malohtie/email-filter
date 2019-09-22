#!/usr/bin/env python3.6

# import the necessary packages
import csv, re, sys
from pathlib import Path
from datetime import datetime


file = input("Drage Your Email List : ")
inputdomain = input("Enter a list of domain aol,yahoo,... : ")
domains = inputdomain.split(",")

found = 0
line = 0
valid = []
date = datetime.now().strftime("%d_%m_%Y_%H_%M_%S");
filename = "./result_filter_"+date+".txt"

my_file = Path(file)
if my_file.is_file():
	with open(format(file)) as csvs:
		emails = csv.reader(x.replace('\0', '') for x in csvs)
		for email in emails:
			if email:
				line +=1
				domain = email[0].strip().lower().split('@');
				if len(domain) == 2:
					for em in domains:
						if domain[1].find(em) != -1:
							found += 1
							#print("EMAIL FOUND : "+email[0])
							valid.append(email[0].strip().lower())
							if(found % 100 == 0):
								print("FOUND "+str(found)+" EMAILS -- CURRENT LINE "+str(line))
							break
	csvs.close()
else:
	print("FILE NOT FOUND")


print("WRITING RESULT BE PATIENT :)")

def is_valid_email(email):
	if len(email) > 7:
		return bool(re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email))

validemail = 0
with open(filename, 'w+', encoding='utf-8') as txt:
	for data in valid:
		if(is_valid_email(data)):
			validemail += 1
			txt.write(data+"\n")


print('ENDED FOUND :'+str(found)+' VALID EMAILS :'+str(validemail))