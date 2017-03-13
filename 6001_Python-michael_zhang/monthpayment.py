# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:22:39 2017

@author: Surface3pro
"""

def calMonBalance(balance, annualInterestRate, monthlyPaymentRate, month):
    if month == 1:
       currentbalance = (balance - balance*monthlyPaymentRate) + (balance - balance*monthlyPaymentRate)*(annualInterestRate/12)
       print(currentbalance)
       return currentbalance
    else:
        currentbalance = (calMonBalance(balance, annualInterestRate, monthlyPaymentRate, month-1)-calMonBalance(balance, annualInterestRate, monthlyPaymentRate, month-1)*monthlyPaymentRate)*(1 + annualInterestRate/12)
        print(currentbalance)
        return currentbalance
        
        
# MIT6001 week2 pset 1      
def calBalance_ite(balance, annualInterestRate, monthlyPaymentRate):
    currentb = balance
    for i in range(0, 12):
        remainb = (currentb - currentb*monthlyPaymentRate)*(1 + annualInterestRate/12)
        #print("Month " + str(i+1) + " Remainning: ",  remainb)
        currentb = remainb
    print("Remaining balance: ", round(remainb, 2))
    #return  round(remainb, 2)
        
#week2 pset 2
def amount_Payoff_(balance, annualInterestRate):
    amount = ((((((balance - amount)*(1+annualInterestRate/12)-amount)*(1+annualInterestRate/12)-amount)*(1+annualInterestRate/12)-amount)*(1+annualInterestRate/12)-amount)*(1+annualInterestRate/12)-amount)*(1+annualInterestRate/12)

    
def amount_Payoff(balance, annualInterestRate):
    originalBalance = balance
    orig_payment = 0
    while balance > 0:
        balance = originalBalance
        orig_payment += 10
        for i in range(12):
            balance = (balance - orig_payment)*(1 + annualInterestRate/12)
    print("Lowest Payment: " + str(orig_payment))
    return orig_payment
    

def amount_Payoff_cent(balance, annualInterestRate):
    originalbalance = balance
    up_bound = round((balance*((1+annualInterestRate/12)**12))/12,2)
    low_bound = round(balance/12, 2)
    payment = round((up_bound + low_bound)/2,2)
    for i in range(12):
        balance = (balance - payment)*(1 + annualInterestRate/12)
    while abs(balance) > 0.01 and up_bound> payment > low_bound:
        if balance > 0.01:
            balance = originalbalance
            low_bound = payment
            payment = round((up_bound + low_bound)/2,2)
            for i in range(12):
                balance = (balance - payment)*(1 + annualInterestRate/12)
        elif -balance > 0.01:
            balance = originalbalance
            up_bound = payment
            payment = round((up_bound + low_bound)/2,2)
            for i in range(12):
                balance = (balance - payment)*(1 + annualInterestRate/12)
    print("lowest payment: " + str(payment))


    
    #and payment > low_bound
'''    
originalbalance = balance
up_bound = round((balance*((1+annualInterestRate/12)**12))/12,2)
low_bound = round(balance/12, 2)
payment = round((up_bound + low_bound)/2,2)
for i in range(12):
    balance = (balance - payment)*(1 + annualInterestRate/12)
while abs(balance) > 0.01 and payment > low_bound:
    if balance > 0.01:
        balance = originalbalance
        low_bound = payment
        payment = round((up_bound + low_bound)/2,2)
        for i in range(12):
            balance = (balance - payment)*(1 + annualInterestRate/12)
    elif -balance > 0.01:
        balance = originalbalance
        up_bound = payment
        payment = round((up_bound + low_bound)/2,2)
        for i in range(12):
            balance = (balance - payment)*(1 + annualInterestRate/12)
print("lowest payment: " + str(payment))
'''
    
    
    
    
    
    
    
    
    
    
    
    
    