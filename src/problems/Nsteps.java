package problems;

/*
Starting from point (0,0) on a plane, we have written all non-negative integers 0, 1, 2,... as shown in the figure.
For example, 1, 2, and 3 has been written at points (1,1), (2,0), and (3, 1) respectively and this pattern has continued.

Illustration:
=============
You are to write a program that reads the coordinates of a point (x, y), 
and writes the number (if any) that has been written at that point. 
(x, y) coordinates in the input are in the range 0...10000.

	y  
	  8|				16
	  7|			  13  15
	  6|			12	14
	  5|		  9	  11
	  4|		8	10
	  3|	  5	  7
	  2|	4	6
	  1|  1   3
	  0|0   2
	  	- - - - - - - - - -
	  	0 1 2 3 4 5 6 7 8 9

Input:
======
The first line of the input is N, the number of test cases for this problem. 
In each of the N following lines, there is x, and y representing the coordinates (x, y) 
of a point.

Output:
=======
For each point in the input, write the number written at that point or write No Number if there is none.

Example:
=======
Input:
3
4 2
6 6
3 4

Output:
6
12
No Number
 */

import java.util.Scanner;
public class Nsteps {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int T = scan.nextInt();

		for (int t=0; t < T; t++) {
			int x = scan.nextInt();
			int y = scan.nextInt();

			boolean isXeven = (x%2 == 0)?true:false;
			boolean isYeven = (y%2 == 0)?true:false;
			
			if ( x < y || x-y > 2
					|| ((isXeven && !isYeven) || (!isXeven && isYeven))) {
				System.out.println("No Number");
			} else {
				if (isXeven)
					System.out.println(x+y);
				else
					System.out.println(x+y-1);
			}
		}

		scan.close();
	}
}
