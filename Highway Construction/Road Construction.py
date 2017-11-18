# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:49:35 2017

@author: aagre
"""

#!/bin/python3

import sys
from sympy import bernoulli
from math import factorial

def highwayConstruction(n, k):
    cost = 0
#    for i in range(1,n-1):
#        cost += (abs(n - i))**k
#    return (cost % 1000000009)
    B = [bernoulli(i) for i in range(k+1)]
    k_factorial = factorial(k)
    for x in range(1,k+2):
        cost += (((-1)**(k-x+1))*B[k-x+1]*k_factorial*(n**x))/(factorial(x)*factorial(k-x+1))
    cost = cost -1 -(n**k)
    return cost%1000000009

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        result = highwayConstruction(n, k)
        print(result)