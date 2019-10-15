# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:52:02 2019

@author: aqsha
"""

import pandas
from collections import Counter
with open("theraven.txt", "r") as thefile:
    duetolist = thefile.read()
mylist = list(duetolist.split(" "))
reversed = sorted(mylist, reverse=True)
mylistcount = Counter(reversed)
df = pandas.DataFrame.from_dict(mylistcount, orient='index')
df.columns.name = 'I colored it'
df.index.name = 'Words'
ax = df.plot(kind='bar', color = 'DarkGreen').set_title('Word count for The Raven');
