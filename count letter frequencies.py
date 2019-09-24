# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
firstw = input("first word : ")
secondw = input("second word : ")
anag1 = sum([ord(x) for x in firstw])
anag2 = sum([ord(y) for y in secondw])
if (anag1 == anag2):
    print("They are anagrams of each other")
else:
    print("They are not anagrams")
    

#%%