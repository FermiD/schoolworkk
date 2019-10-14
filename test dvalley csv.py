# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:58:57 2019

@author: aqsha
"""

import csv
import matplotlib.pyplot as plt

x = []
y = []

with open(r'C:\Users\aqsha\.spyder-py3\PROJECTS\weatherbook.csv', 'r') as g:
    plots = csv.reader(g, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, marker='o')

plt.title('Weather for Death Valley, 2014')

plt.xlabel('Date')
plt.ylabel('Temperature in F')

plt.show()