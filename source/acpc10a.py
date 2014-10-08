'''
Created on Oct 3, 2014

@author: karthik
'''

T = raw_input()
while T != "0 0 0":
    T = T.split(" ")
    a1 = int(T[0])
    a2 = int(T[1])
    a3 = int(T[2])
    
    v1 = a2-a1
    v2 = a3-a2
    
    if v1 == v2:
        print a3+v1
    else:
        print a3*(v2/v1)
    
    T = raw_input()