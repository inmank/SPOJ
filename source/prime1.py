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
    outArr = range(minVal, maxVal);
    
    #Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(maxVal))+1):
        for j in range(0, len(outArr)):
            if j >= len(outArr):
                break
            
            val = outArr[j]
            
            if (val % i == 0 and (i != 1 or i != j)):
                    outArr.remove(val)
            
    for k in range(0, len(outArr)):
        print outArr[k]
                            
    print "";
