'''
Created on Jul 29, 2014

@author: karthik

You are asked to calculate factorials of some small positive integers.

Input

An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single 
integer n, 1<=n<=100.

Output

For each integer n given at input, display a line with the value of n!

Example

Sample input:
4
1
2
5
3
Sample output:

1
2
120
6
'''
def facto(n):
    if n >2:
        n*=facto(n-1);

    return n;

for i in range(int(raw_input())):
    print facto(int(raw_input()));