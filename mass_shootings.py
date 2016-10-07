# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:10:42 2016

@author: brunogtavares
"""
# In this data I'm interested to know:
# - the amout of mass shootings from 1982 - 2014
# - proportion of people in favor of gun control laws from 1982-2014

import csv as csv
import numpy as np

csv_file = csv.reader(open('mj-1982-2016-US-mass-shootings.csv', 'rb'))
header = csv_file.next()

data = []

for row in csv_file:
    data.append(row)
data = np.array(data)

new_data = open("mass_shootings_per_year.csv", "wb")
new_data_object = csv.writer(new_data)
new_data_object.writerow(["Year", "MassShootings"])

ms_count = {}


for row in data:
    ms_count[row[3]] = ms_count.get(row[3], 0) + 1
print ms_count

for year in range(1982, 2017):
    if str(year) in ms_count:
        year = str(year)
        new_data_object.writerow([year, ms_count[year]])
