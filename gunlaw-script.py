# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:46:42 2016

@author: brunogtavares
"""
# In this data I'm interested to know:
# - the average age
# - the average age of who's in favor
# - the average age of who's opposed
# - proportion of people in favor throughout the years

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('tdgunlaw.csv', 'rb'))

header = csv_file_object.next()
data = []

for row in csv_file_object:
    data.append(row)

data = np.array(data)

first_year = np.int(data[0, 1])
last_year = np.int(data[-1, 1]) + 1


new_data = open("gunlaw_opinion.csv", "wb")
new_data_object = csv.writer(new_data)
new_data_object.writerow(["Year", "Total", "AverageAge", "GunLaw-Favor", "GLF-AvgAge", "GunLaw-Oppose", "GLO-AvgAge"])

af = open("age_frequency.csv", "wb")
age_frequency = csv.writer(af)
age_frequency.writerow(["Year", "Age_Frequency", "FavorAgeFrquency", "OpposeAgeFrequency"])

frequency = {}
FavorAgeFrequency = {}
OpposeAgeFrequency = {}
total_people = 0

for year in range(first_year, last_year):
    oppose = 0
    favor = 0
    age = 0
    fage = 0
    oage = 0
    total = 0
    for row in data:
        if  row[1] == str(year):
            if row[-1] == 'FAVOR':
                favor += 1
                fage += int(row[5])
                FavorAgeFrequency[row[5]] = FavorAgeFrequency.get(row[5],0) + 1
            elif row[-1] == 'OPPOSE':
                oppose += 1
                oage = int(row[5])
                OpposeAgeFrequency[row[5]] = OpposeAgeFrequency.get(row[5],0) + 1

            age += int(row[5])
            frequency[row[5]] = frequency.get(row[5],0) + 1
            total += 1

    if total == 0: continue

    gunlaw_favor = round(float(favor) / float(total), 3)
    glf_avgage = round(float(fage) / float(favor))
    gunlaw_oppose = round(float(oppose) / float(total), 3)
    glo_avgage = round(float(oage) / float(oppose), 3)
    average_age = round(float(age) / float(total), 3)
    total_people += total

    age_frequency.writerow([year, frequency, FavorAgeFrequency, OpposeAgeFrequency])

    print year, gunlaw_favor, glf_avgage, gunlaw_oppose, glo_avgage, average_age, total_people

    new_data_object.writerow([year, total_people, average_age, gunlaw_favor, glf_avgage, gunlaw_oppose, glo_avgage])
