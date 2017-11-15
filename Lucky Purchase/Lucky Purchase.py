#!/bin/python3

import sys
import math

if __name__ == "__main__":
    n = int(input().strip())
    min_val = math.inf
    min_val_name = ""
    for a0 in range(n):
        flag = False
        count_flag = False
        name, value = input().strip().split(' ')
        name, value = [str(name), int(value)]
        if len(str(value))%2 == 0:
            count4 = 0
            count7 = 0
            for i in str(value):
                if i == "4":
                    count4 +=1
                    flag = True
                elif i == "7":
                    count7 +=1
                    flag = True
                else: 
                    flag = False
                    break;
            if count4 == count7:
                count_flag = True
        if flag and count_flag:
            if min_val > value:
                min_val = value
                min_val_name = name
                 
    if min_val == math.inf:
        print("-1")
    else:
        print(min_val_name)
