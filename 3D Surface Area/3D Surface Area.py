# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:07:26 2017

@author: aagrekar
"""

#!/bin/python3

import sys

def surfaceArea(A):
    nrows = len(A)
    ncols = len(A[0])
    top_surface_area = nrows*ncols
    bottom_surface_area = nrows*ncols
    right_surface_area = 0
    left_surface_area = 0
    up_surface_area = sum(A[0][:])
    down_surface_area = sum(A[nrows-1][:])
    other_uncovered_area = 0
    
    for i in range(nrows):
        left_surface_area += A[i][0]
        right_surface_area += A[i][ncols-1]
    
    for i in range(nrows):
        j=0
        while j < (ncols-1):
            other_uncovered_area += abs(A[i][j]-A[i][j+1])
            j+=1
    
    for j in range(ncols):
        i = 0
        while i < (nrows-1):
            other_uncovered_area += abs(A[i][j]-A[i+1][j])
            i+=1
    return top_surface_area+bottom_surface_area+up_surface_area+down_surface_area+right_surface_area+left_surface_area+other_uncovered_area
    
if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A)
    print(result)
