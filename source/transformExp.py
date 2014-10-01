'''
Created on Oct 1, 2014

@author: karthik

Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). 
Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ). Operands: only letters: a,b,...,z. 
Assume that there is only one RPN form (no expressions like a*b*c).

Input

t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
Text grouped in [ ] does not appear in the input file.

Output

The expressions in RPN form, one per line.
Example

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
'''

def transform(expIn):
    rpn = ""
    expIn = str(expIn)
    if (len(expIn) == 1):
        rpn = rpn + expIn
    elif (len(expIn) == 3):
        rpn= rpn + expIn
        
'''
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

///(a+(b*c))
public class TransformExp {
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
'''