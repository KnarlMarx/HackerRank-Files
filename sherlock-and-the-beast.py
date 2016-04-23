#!/bin/python3

import sys

def sherlock(num_array):
    for i in range(len(num_array)):
        num = -1
        
        if(num_array[i] % 5 == 0):
            num = ''
            for k in range(num_array[i]):   
                num = num + '3'
            
        for j in range(num_array[i],0,-1):
            if(j % 3 == 0):
                if((num_array[i] - j) % 5 == 0):
                    five_count = j
                    three_count = num_array[i]-j
                    num = ''
                    
                    if(three_count == 0):
                        for k in range(five_count):   
                            num = num + '5'
                              
                    else:    
                        for k in range(((num_array[i])-(five_count)),(num_array[i])):
                            num = num + '5'
                                 
                        for l in range(three_count):
                            num = num + '3'  
                    break
                
        print(num)
    
t = int(input().strip())
l = []
for a0 in range(t):
    n = int(input().strip())
    l.insert(a0,n)

sherlock(l)

    

