package problems;

import java.util.Scanner;
import java.util.StringTokenizer;

///(a+(b*c))
public class ONP {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int T = scan.nextInt();

		for (int t=0; t < T; t++) {
			String exp = scan.next();
			StringTokenizer sTok = new StringTokenizer(exp, "()+-*/^", true);
			System.out.println(transform(sTok));
		}

		scan.close();
	}

	private static String transform(StringTokenizer sTok) {
		String str = "";
		String sym = "";
		while(sTok.hasMoreTokens()) {
			String tok = sTok.nextToken();

			if (tok.equals("(")){
				str = str + transform(sTok);
			} else if (tok.equals(")")){
				return (str + sym);
			} else if (tok.equals("+") || tok.equals("-") || tok.equals("*") 
					|| tok.equals("/") || tok.equals("^")) {
				sym = tok;
			} else {
				str = str + tok;
			}
		}
		return str;
	}
}