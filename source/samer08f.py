'''
Created on Oct 2, 2014

@author: karthik
'''

N = int(raw_input())
while N != 0:
    total = 0
    for k in range(0, N):
        val = N-k
        total = total + (val*val)
    
    print total
    N = int(raw_input())