#!/bin/python3

import sys


t = int(input().strip())
l = []
thres = []
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    thres.append(k)
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    l.append(a);

for i in range(len(l)):
    ontime = 0
    late = 0
    for j in range(len(l[i])):
        if (l[i][j] <= 0):
            ontime += 1
        elif (l[i][j] > 0):
            late += 1
    if (ontime < thres[i]):
        print ("YES")
    else:
        print ("NO")
     
