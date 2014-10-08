package problems;

import java.util.Scanner;

public class Samer08F {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		while (N != 0) {
			long total = 0;
			for (int k =0; k < N; k++){
				int val = N-k;
				total +=(val*val);
			}

			System.out.println(total);
			N = scan.nextInt();
		}
		scan.close();		
	}
}
