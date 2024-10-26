import java.util.Scanner;
public class MinimumCharactersToMakePalindrome {
    public static int[] computeLPSArray(String str) {
        int len = 0;
        int i = 1;
        int n = str.length();
        int[] lps = new int[n];
        lps[0] = 0; 
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
    public static int minCharsToMakePalindrome(String str) {
        String reversedStr = new StringBuilder(str).reverse().toString();
        String combinedStr = str + "#" + reversedStr; 
        int[] lps = computeLPSArray(combinedStr);
        int longestPalindromicSuffixLength = lps[lps.length - 1];
        return str.length() - longestPalindromicSuffixLength;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine().trim();
        int result = minCharsToMakePalindrome(str);
        System.out.println(result);
    }
}
