'''
Created on Jun 8, 2014

@author: karthik

Problem:

Your program is to use the brute-force approach in order to find the Answer 
to Life, the Universe, and Everything. More precisely... 
rewrite small numbers from inVal to output. Stop processing inVal after 
reading in the number 42. 
All numbers at inVal are integers of one or two digits.

Example

Input:
1
2
88
42
99

Output:
1
2
88
'''
        
inVal = raw_input()
while (int(inVal) != 42):
    print int(inVal)
    inVal = raw_input()