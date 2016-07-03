#!/bin/python3

import sys

count = 0
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for i in range(0,(n+1)):
    for j in range(0,(n+1)):
        if(i < j):
            if(((a[i]+a[j]) % k) == 0):
                count += 1
        else:
            continue

print (count)
