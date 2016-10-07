# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:46:42 2016

@author: brunogtavares
"""
# In this data I'm interested to know:
# - the amout of mass shootings from 1982 - 2014
# - proportion of people in favor of gun control laws from 1982-2014

import csv as csv
import numpy as np

csv_gl = csv.reader(open('gunlaw_opinion.csv', 'rb'))
gl_header = csv_gl.next()

csv_mj = csv.reader(open('mass_shootings_per_year.csv', 'rb'))
mj_header = csv_mj.next()

gl_data = []
for row in csv_gl:
    gl_data.append(row)
gl_data = np.array(gl_data)

data = []
for row in csv_mj:
    data.append(row)
data = np.array(data)


new_data = open("gunlaws_mass_shootings.csv", "wb")
new_data_object = csv.writer(new_data)
new_data_object.writerow(["Year", "Total", "AverageAge", "GunLaw-Favor", "GLF-AvgAge", "GunLaw-Oppose", "GLO-AvgAge", "MassShootings"])


for glrow in gl_data:
    for row in data:
        if glrow[0] in row[0]:
            new_data_object.writerow([glrow[0], glrow[1], glrow[2], glrow[3], glrow[4], glrow[5], glrow[6], row[1]])
