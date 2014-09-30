'''
Created on Jul 29, 2014

@author: karthik

Peter wants to generate some prime numbers for his cryptosystem. 
Help him! Your task is to generate all prime numbers between two given numbers!

Input

The input begins with the number t of test cases in a single line (t<=10). 
In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated 
by a space.

Output

For every test case print all prime numbers p such that m <= p <= n, one number per line, 
test cases separated by an empty line.

Example

Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
'''
import math;
import datetime;

MAX = 1000000000
SMAX = int(math.sqrt(MAX))+1

def seive1(minVal, maxVal):
    outArr = [2]
    if (minVal < 3):
        minVal = 3
        
    if (minVal % 2 == 0):
        minVal+=1;
    
    for j in range(minVal, maxVal, 2):
        isPrime = True
        cap = int(math.sqrt(j))+1
        
        for i in outArr:
            if (i >= cap):
                break
            if (j % i == 0):
                isPrime = False
                break
        
        if isPrime:
            outArr.append(j)
        
    return outArr
    
def seive(minVal, maxVal, sArr):
    #Sieve of Eratosthenes
    '''for i in sArr:
        for j in arrIn:
            if (j != 1 and j != i and j % i == 0):
                arrIn.remove(j)'''

    for i in range(minVal, maxVal, 2):
        cap = int(math.sqrt(i))+1
        isPrime = True
        
        for j in sArr:
            if (j >= cap):
                break
            if (i % j == 0):
                isPrime = False
                break
        
        if isPrime:
            print i
                   
'''def printArr(arr):
    for k in arr:
        print str(k) + " "'''
        
#seiveArr = range(2, SMAX)
seiveArr = seive1(2, SMAX)

#print "Enter now"

for i in range(int(raw_input())):
    inValues = raw_input().split(" ")
    minVal = int(inValues[0])
    if (minVal % 2 == 0):
        minVal+=1;
    maxVal = int(inValues[1])
    print datetime.datetime.now()
    seive(minVal, maxVal, seiveArr)
    #outArr = seive1(minVal, maxVal)
    #printArr(outArr)
                            
    print ""
    #print len(outArr)
    #print ""
print datetime.datetime.now()