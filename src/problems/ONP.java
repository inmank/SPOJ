package problems;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

///(a+(b*c))
public class ONP {
	private static String outstr;

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int T = scan.nextInt();

		for (int t=0; t < T; t++) {
			outstr = "";
			String exp = scan.next();
			transform(exp);
			System.out.println(outstr);
		}

		scan.close();
	}

	private static void transform(String exp) {
		if (exp.startsWith("(") && exp.endsWith(")"))
			exp = exp.substring(1, exp.length()-1);

		Pattern pattern = Pattern.compile("[a-z\\)][\\+\\-\\*\\/\\^][a-z\\(]");
		Matcher matcher = pattern.matcher(exp);

		int start = exp.indexOf(")");
		if (start == -1 || start == exp.length()-1)
			start = 0;

		if (matcher.find(start)) {
			int index = matcher.start() + 1;
			transform(exp.substring(0, index));
			transform(exp.substring(index+1));
			outstr = outstr + exp.charAt(index);
		} else {
			outstr = outstr + exp;
		}
	}
}