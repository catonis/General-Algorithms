# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 04:55:19 2020

@author: Chris Mitchell
"""

def makeChange(amount, denominations):
    """Compute the number of unique ways to make change for the given
       amount using denominations in a passed list."""
       
    table = [[0 for i in range(amount + 1)] for j in range(len(denominations) + 1)]
    
    #For amount 0, there is always one way to make change, and that is not to.
    for i in range(len(table)):
        table[i][0] = 1
    
    #For all positive amounts, you cannot make change with no denominations.
    #Thus the top row remains all zeros (except the first).

    
    #Sort denominations from smallest to largest
    denominations.sort()
    
    #For every integer amount up to the passed value
    for i in range(1, amount + 1):
        #For every donimination
        for j in range(1, len(denominations) + 1):
            waysWithoutNewDenomination = table[j - 1][i]
            if i - denominations[j - 1] < 0:
                waysWithNewDenomination = 0
            else:
                waysWithNewDenomination = table[j][i - denominations[j - 1]]
            table[j][i] = waysWithoutNewDenomination + waysWithNewDenomination
    
    return table
            