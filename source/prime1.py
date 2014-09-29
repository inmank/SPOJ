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

MAX = 1000000000
SMAX = int(math.sqrt(MAX))+1

def seive(arrIn, sArr):
    #Sieve of Eratosthenes
    '''for i in sArr:
        for j in arrIn:
            if (j != 1 and j != i and j % i == 0):
                arrIn.remove(j)'''

    for i in arrIn:
        print str(i) + " "
        for j in sArr:
            if (i == 1 or i == j):
                break
            if (i % j == 0):
                arrIn.remove(i)
                break
                
def printArr(arr):
    for k in arr:
        print str(k) + " "
        
seiveArr = range(2, SMAX)
tmpArr = range(2, int(math.sqrt(SMAX))+1)
seive(seiveArr, tmpArr)

#print "Enter now"
for i in range(int(raw_input())):
    inValues = raw_input().split(" ")
    minVal = int(inValues[0])
    maxVal = int(inValues[1])+1
    outArr = range(minVal, maxVal)
    
    seive(outArr, seiveArr)
    printArr(outArr)
                            
    print ""
    #print len(outArr)
    #print ""
