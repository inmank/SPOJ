package problems;

import java.util.ArrayList;
import java.util.Scanner;

public class Prime1 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		ArrayList<Integer> seiveArr = new ArrayList<Integer>();

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

		scan.close();
	}
}
