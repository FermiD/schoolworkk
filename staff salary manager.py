# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:06:23 2019

@author: aqsha
"""
import re
w = 0

prompt = str(input("What to do next? 1. New Staff, \n 2. Delete Staff, \n 3. Current Staff Salaries, \n 4. Exit"))

dict_staff = dict()
while (prompt != "quit"):
    if (prompt == "new staff"):
        staffname = input("Create staff name= ")
        rlname = input("Input his real name= ")
        if staffname != None:
            if not re.search("[0-9]", staffname[1:4]):
                staffname = str(input("Wrong format. Try again. "))
            if not re.search("S", staffname[0]):
                staffname = str(input("Wrong format. Try again. "))
            if len(staffname) > 20:
                staffname = str(input("Wrong format. Try again. "))
            else:
                position = input("What position in company? Staff, Officer or Manager?")
                if position == "staff":
                   staffpos = print("His/her salary will be: 3500000-7000000")
                   print(staffpos)
                   dict_staff[staffname] = position
                   print(rlname, dict_staff[staffname])
                   prompt = str(input("What to do next? 1. New Staff, \n 2. Delete Staff, \n 3. Current Staff Salaries, \n 4. Exit"))
                if position == "officer":
                    offpos = print("His/her salary will be: 7000001-10000000")
                    print(offpos)
                    dict_staff[staffname] = position
                    print(rlname, dict_staff[staffname])
                    prompt = str(input("What to do next? 1. New Staff, \n 2. Delete Staff, \n 3. Current Staff Salaries, \n 4. Exit"))
                if position == "manager":
                   managpos = print("His/her salary will be greater than 10000000")
                   print(managpos)
                   dict_staff[staffname] = position
                   print(rlname, dict_staff[staffname])
                   prompt = str(input("What to do next? 1. New Staff, \n 2. Delete Staff, \n 3. Current Staff Salaries, \n 4. Exit"))
            if staffname == None:
                staffname = input("Nothing inputted. Try again.")
                
    if (prompt == "delete staff"):
        namostaff = input("Which staff to delete? ")
        if namostaff in dict_staff:
            del dict_staff[namostaff]
            print("Succesfully deleted!")
            prompt = str(input("What to do next? 1. New Staff, \n 2. Delete Staff, \n 3. Current Staff Salaries, \n 4. Exit"))
        else:
            namostaff = str(input("Hm, not found. input again. "))
    if (prompt == "current staff salaries"):
        while w < 1:
            print(dict_staff)
            w += 1
        prompt = str(input("What to do next? 1. New Staff, \n 2. Delete Staff, \n 3. Current Staff Salaries, \n 4. Exit"))
    if (prompt == "exit"):
        break