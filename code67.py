import java.util.Scanner;
public class MinimumCharsToPalindrome {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        int result = minCharsToMakePalindrome(str);
        System.out.println(result);
    }
    public static int minCharsToMakePalindrome(String str) {
        String concat = str + "#" + new StringBuilder(str).reverse().toString();
        int[] lps = computeLPS(concat);
        return str.length() - lps[lps.length - 1];
    }
    private static int[] computeLPS(String str) {
        int n = str.length();
        int[] lps = new int[n];
        int len = 0;
        int i = 1;
        while (i < n) {
            if (str.charAt(i) == str.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
}
