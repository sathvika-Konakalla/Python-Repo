import java.util.Scanner;
public class DecodeString {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        while (T-- > 0) {
            int N = scanner.nextInt(); 
            int K = scanner.nextInt(); 
            String finalString = scanner.next(); 
            String originalString = decodeString(finalString, N, K);
            System.out.println(originalString);
        }
    }
    private static String decodeString(String finalString, int N, int K) {
        char[] chars = finalString.toCharArray();
        for (int i = K; i >= 1; i--) {
            reverse(chars, i);
        }
        return new String(chars); 
    }
    private static void reverse(char[] chars, int length) {
        int left = 0, right = length - 1;
        while (left < right) {
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }
    }
}
