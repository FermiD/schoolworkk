# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#using dictionary, attempt
#%%
numeral = str(input("Insert roman numeral to be convert: "))
def romanconvert(numeral):
    rome = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    norm = 0
    for i in range(len(numeral)):
        if i > 0 and (rome[numeral[i]]) > rome[numeral[i - 1]]:
            norm += rome[numeral[i]] - (2 * rome[numeral[i-1]])
        else:
            norm += rome[numeral[i]]
    return norm

print(romanconvert(numeral))
print("ROMA")


#%%