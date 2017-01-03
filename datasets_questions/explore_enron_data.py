#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#the enron data
print enron_data

#Number of people in the enron dataset
print "number of people: "
print len(enron_data)

#Number of features per person
print "features per person: "
print len(enron_data["SKILLING JEFFREY K"])

#Number of "POIs" (aka person of interest) in the enron dataset
count = 0
for k, v in enron_data.items():
    if v["poi"] == True:
        count += 1
print "poi's: "
print count

#How many POIs Exist in poi_names.txt?
poi_names = open("../final_project/poi_names.txt").read().split('\n')
poi_y = [name for name in poi_names if "(y)" in name]
poi_n = [name for name in poi_names if "(n)" in name]
print "number of people in poi_names.txt: "
print len(poi_y + poi_n)

#Like any dict of dicts, individual people/features can be accessed like so:
#enron_data["LASTNAME FIRSTNAME"]["feature_name"]
#or, sometimes 
#enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]
#What is the total value of the stock belonging to James Prentice?
print "total value of the stock belonging to James Prentice: "
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

#How many email messages do we have from Wesley Colwell to persons of interest?
print "email messages do we have from Wesley Colwell to persons of interest:"
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#What’s the value of stock options exercised by Jeffrey K Skilling?
print "value of stock options exercised by Jeffrey K Skilling:"
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

#Of Lay, Skilling, and Fastow, who took home the most money? How much money was it?
print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])

#How many folks in the dataset have a quantified salary?
print "folks in the dataset with a quantified salary:"
count_salary = 0
for k, v in enron_data.items():
    if v["salary"] != 'NaN':
        count_salary += 1
print count_salary

#Known email address?
print "folks in the dataset with an email address:"
count_email = 0
for k, v in enron_data.items():
    if v["email_address"] != 'NaN':
        count_email += 1
print count_email

#How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?
print "folks in the dataset with NaN for their total payments:"
count_total_payments = 0
for k, v in enron_data.items():
    if v["total_payments"] == 'NaN':
        count_total_payments += 1
print count_total_payments

#How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
print "POIs in the dataset with NaN for their total payments:"
count_total_payments = 0
for k, v in enron_data.items():
    if v["poi"] == True and v["total_payments"] == 'NaN':
        count_total_payments += 1
print count_total_payments

#If a machine learning algorithm were to use total_payments as a feature, would you expect it to associate a “NaN” value with POIs or non-POIs?
#answer: non-POIs

#If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change.
#What is the new number of people of the dataset? 
#answer #1: number in dataset = 156
#What is the new number of folks with “NaN” for total payments?
#answer #2: "NaN for total payments" = 31
#What is the new number of POI’s in the dataset?
#answer #3: 28
#What is the new number of POI’s with NaN for total_payments?
#answer #4: 10
#Once the new data points are added, do you think a supervised classification algorithm might interpret “NaN” for total_payments as a clue that someone is a POI?
#yes