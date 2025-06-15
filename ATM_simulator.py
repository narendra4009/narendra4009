# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 22:28:39 2025

@author: Narendra

Task: Real Time ATM Simulation

1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit

"""
while True:
        
    print("*******Welcome To ATM*******")
    balance = 100000 # Existing Balance
    machine_amount = 200000
    
    print('Choose Your Option:')
    print('1. Check Balance:')
    print('2. Withdraw Money')
    print('3. Deposit Money')
    print('4. Exit')
    
    choice = eval(input("Enter Your Choice:"))
    
    if choice > 0 and choice <= 4:
        if choice == 1:
            print('Your Current Balance Is: {}/-'.format(balance))
            
        elif choice == 2:
            withdraw_amount = eval(input('Enter Amount To Withdraw:'))
            
            if withdraw_amount <= balance and withdraw_amount <= machine_amount:
                balance = balance - withdraw_amount
                print('{}/- Withdraw successfully!!!'.format(withdraw_amount))
                print("Remaining Balance is: {}/-".format(balance))
            else:
                print('Insufficient Balance')
                
        elif choice == 3:
            deposit_amount = eval(input("Enter Amount To Deposit:"))
            if deposit_amount > 0:
                balance = balance + deposit_amount
                print("{}/- Deposited Successfully!!".format(deposit_amount))
                print('Current Balance is:{}/-'.format(balance))
            else:
                print('Invalid Deposit Amount!!')
        
        else:
            print('Thank You For Using ATM')
            break
            
    else:
        print('Invalid Choice and Enter your choice between 1 To 4')