# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:12:53 2019

@author: aqsha
"""

class Bank_Acc:
    def __init__(self):
        self.balance=100
        print("Hello. Welcome to the machine.")
        
    def deposit(self):
        amt = float(input("Enter deposit amount >> "))
        self.balance += amt
        print("\n amount deposited: ",amt)
        
    def withdrawal(self):
        amt = float(input("Enter withdrawal amount >> "))
        if self.balance >= amt:
            self.balance -= amt
            print("\n You withdrew: ", amt)
        else:
            print("\n insufficient funds")
            
    def displayer(self):
        print("\n current balance: ", self.balance)
        
s = Bank_Acc()
s.deposit()
s.withdrawal()
s.displayer()