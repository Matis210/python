# -*- coding: utf-8 -*-
from cardholder import Cardholder
import random
import time

def print_menu():
    print("Please choose one of these following options... ")
    print("1. Deposit ")
    print("2. Withdraw ")
    print("3. Show Balance")
    print("4. Exit ")
    
def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ you want to deposit?: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your $$. Your new balance is: "+ str(cardHolder.get_balance()))
    except:
        print("Value error")
        
def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ you want to withdraw?: "))
        if(cardHolder.get_balance()< withdraw):
                ## if accType = "S" then enabled balance overdraft to -300 
                if(cardHolder.get_accType()=="S" and (cardHolder.get_balance() - withdraw) >= -300):
                    cardHolder.set_balance(cardHolder.get_balance() - withdraw)
                    print("You good to go. Thank you") 
                else:
                    print("Insuficient balance")
        else:
           cardHolder.set_balance(cardHolder.get_balance() - withdraw)
           print("You good to go. Thank you")   
    except:
        print("Value error")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())
  
def gen_cardNum():
    CN = str(random.randint(100000, 1000000))
    PIN = str(random.randint(1000, 9999))
    print(CN, " : ",PIN)
     
  
if __name__ == "__main__":
    current_user = Cardholder("", "", "", "", "", "") 
    
    #gen_cardNum() - just used for gen random cardNum + PIN
    
    ### create repo of users
    list_of_cardHolders = []
    list_of_cardHolders.append(Cardholder("529633", 6008, "Matus", "Potucek", 5000, "S" ))
    list_of_cardHolders.append(Cardholder("182038", 2161, "Robert", "Kaiser", 2000, "C" ))
    list_of_cardHolders.append(Cardholder("367442", 2640, "Monika", "Potuckova", 3000, "C" ))
    list_of_cardHolders.append(Cardholder("771372", 4585, "Martina", "Potuckova", 7000, "S" ))
    
### prompt user for debit card
    debit_cardNum = ""
    while True:
        try:
            debit_cardNum = input("Please insert your debit card: ")
            ## check against our repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debit_cardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again")
        except:
            print("Card number not recognized. Please try again.")
### Prompt for PIN ,max attempts are set to 3
    max_attempts = 3
    attempts = 1
    while True:
        try:
            userPIN= int(input("Please enter your PIN: ").strip())
            if(int(current_user.get_PIN()) == userPIN):
                break
            else:
                if(attempts == max_attempts):
                    break
                attempts += 1
                time.sleep(0.5)
                print("Invalid PIN, please try again")
        except:
            time.sleep(0.5)
            print("Invalid PIN, please try again")
                
    ### print options
    if(attempts < max_attempts):     
        print("Welcome ",current_user.get_firstName(),"!")
        option = 0
        while True:
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid input, please try again.")    
            if option == 1:
                deposit(current_user)
            elif option == 2:
                withdraw(current_user)
            elif option == 3:
                check_balance(current_user)
            elif option == 4:
                time.sleep(0.5)
                break 
        
        print("Thank your for using our terminal.")
    else:
        print("Max attempts reached, you will need to insert your card again.")