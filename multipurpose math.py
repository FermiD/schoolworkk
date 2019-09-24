# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
tkst = input("Enter sentence: ")
searchl = str(input("Which letter to count? "))
cnt = 0
for i in range(len(tkst)):
    cnt = tkst.count(searchl)
print("There are ", cnt, "letters of", searchl)
    


#%%