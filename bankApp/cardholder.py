# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:52:18 2024

@author: matus
"""

#accType - C: classic, S: super

class Cardholder():
    def __init__(self,cardNum,PIN,firstName,lastName,balance,accType):
        self.cardNum = cardNum
        self.PIN = PIN
        self.firstName = firstName
        self.lastName= lastName
        self.balance = balance
        self.accType = accType
       
    ### Getter methods
    def get_cardNum(self):
        return self.cardNum
    def get_PIN(self):
        return self.PIN
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_balance(self):
        return self.balance
    def get_accType(self):
        return self.accType
        
    ### Setter methods
    def set_cardNum(self, newVal):
        self.cardNum = newVal
    def set_PIN(self, newVal):
        self.PIN = newVal
    def set_firstName(self, newVal):
        self.firstName = newVal
    def set_lastName(self, newVal):
        self.lastName = newVal
    def set_balance(self, newVal):
        self.balance = newVal
    def change_accType(self):
        if(self.accType=="C"):
             self.accType = "S"      
        else:
            self.accType = "C"        
           
        
    def print_out(self):
        print("Card # :",self.cardNum)
        print("PIN :",self.PIN)
        print("First Name :",self.firstName)
        print("Last Name :",self.lastName)
        print("Balance :",self.balance)
        print("Acc type: ",self.accType)
        
