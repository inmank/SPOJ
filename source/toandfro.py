'''
Created on Oct 2, 2014

@author: karthik
'''

C = int(raw_input())
while C != 0:
    cipher = raw_input();
    R = len(cipher)/C
    
    message = [[0 for n in range(C)] for m in range(R)]
    
    row = 0
    col = 0
    isTo = True
    for index, char in enumerate(cipher):
        if (index >= C and (index%C) == 0):
            row+=1
            isTo = not isTo
            col = 0 if isTo else C-1
            
        message[row][col] = char
        col = col+1 if isTo else col-1
    
    outstr = ""
    for i in range(len(message[0])):
        for r in message:
            outstr = outstr + str(r[i]) 
    
    print outstr      
    C = int(raw_input())
    
    
    
    
    
    