# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:35:48 2017

@author: aagre
"""

def main():
    n, m, k = map(int,input().strip().split());
    a = [[0 for x in range(n)] for y in range(n)] 
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                a[i][j] = m
            elif i == j:
                a[i][j] = a[i-1][j-1] + k
            elif i<j:
                a[i][j] = a[i][j-1] - 1
            else:
                a[i][j] = a[i-1][j] -1
    
    for i in range(n):
        row_ele = ""
        for j in range(n):
            row_ele += str(a[i][j]) + " "
        print(row_ele)
    
if __name__ == "__main__":
    main()