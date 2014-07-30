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

for i in range(int(raw_input())):
    inValues = raw_input().split(" ");
    minVal = int(inValues[0]);
    maxVal = int(inValues[1])+1;
    
    #Trivial ways
    '''for j in range(minVal, maxVal):
        if (j == 2): print j;
         
        if (j == 1 or j%2 == 0):
            continue;
        
        isPrime = True;
        for count in range(3, int(math.sqrt(j))+1):
            if (j%count == 0):
                isPrime = False; 
                break;
        
        if(isPrime): print j;'''
        
    #Seive of Erothesenes
    '''seiveArr = range(minVal, maxVal);
    index = 0;
    
    if 1 in seiveArr:
        seiveArr.remove(1);
        
    while (index < len(seiveArr)):
        p = seiveArr[index];
        count = 2;
        num = p*count;
        while (num <= seiveArr[-1]):
            if num in seiveArr:
                seiveArr.remove(num);
            count+=1;
            num = p*count;
        
        index+=1;
        
    for prime in seiveArr:
        print prime;'''
    
    seiveArr = range(2, math.sqrt(maxVal));
    outArr = range(minVal, maxVal);
    print "";
