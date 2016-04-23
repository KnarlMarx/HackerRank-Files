#!/bin/python3

import sys

def utopianTree(num_array):
    for i in range(len(num_array)):
        #reset total after each iteration
        total = 0
        j = 0
        while (j <= num_array[i]):
            if(j % 2 == 0 or j == 0) :
                total = total + 1
            else:
                total = total * 2
            j+= 1
            
        print(total)



t = int(input().strip())
l = []
for a0 in range(t):
    n = int(input().strip())
    l.insert(a0,n)

utopianTree(l)
