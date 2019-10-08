# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 07:39:31 2019

@author: aqsha
"""
import random
from wwtbamans import *
name = input("what is your name? ")

global ans

for x in range(0, 5):
    number = random.randrange(0, 20)
    print (question[number])
    print ("your choices are: ", choices[number])
    ans = input("Select the correct answer: ")
    checkanswer(ans) 
points = 0

def checkanswer(ans):
    global points
    if ans == answerz[number]:
        points += 100
        print("Your answer is correct! Your total earnings are: ", (points * 50))
    else:
        print("Wrong answer! Try again.")   