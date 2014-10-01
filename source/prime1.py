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
                   
seiveArr = seive1(2, SMAX)

#print "Enter now"

for i in range(int(raw_input())):
    inValues = raw_input().split(" ")
    minVal = int(inValues[0])
    maxVal = int(inValues[1])
    
    if (minVal % 2 == 0):
        minVal+=1;
        
    
    #print datetime.datetime.now()
    seive(minVal, maxVal, seiveArr)
                            
    print ""

#print datetime.datetime.now()


'''
Java

import java.util.ArrayList;
import java.util.Scanner;

public class PrimeGen {
    Scanner scan = new Scanner(System.in);
    ArrayList<Integer> seiveArr = new ArrayList<Integer>();
    
    private void genSeive() {
        seiveArr.add(2);
        for (int i=3; i < 32000; i+=2) {
            boolean isPrime = true;
            int cap = (int) Math.sqrt(Double.valueOf(i)) + 1;

            for (int j : seiveArr) {
                if ( j >= cap) break;

                if (i%j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
                seiveArr.add(i);
        }
    }
    
    private void genPrime() {
        int totalCase = scan.nextInt();

        for (int k = 0; k < totalCase; k++) {
            if (k > 0) System.out.println("");

            int minVal = scan.nextInt();
            int maxVal = scan.nextInt();

            if (minVal < 3) {
                minVal = 3;
                System.out.println(2);
            }

            if (minVal %2 == 0) minVal +=1;

            for (int i=minVal; i <= maxVal; i+=2) {
                boolean isPrime = true;
                int cap = (int) Math.sqrt(Double.valueOf(i)) + 1;

                for (int j : seiveArr) {
                    if ( j >= cap) break;

                    if (i%j == 0) {
                        isPrime = false;
                        break;
                    }
                }

                if (isPrime)
                    System.out.println(i);
            }
        }
    }
    
    public static void main(String[] args) {
        PrimeGen pp = new PrimeGen();
        pp.genSeive();
        pp.genPrime();
    }

}
'''