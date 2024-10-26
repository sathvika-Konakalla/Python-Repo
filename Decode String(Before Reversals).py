import java.util.Scanner;
public class DecodeString {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); 
        scanner.nextLine(); 
        for (int t = 0; t < T; t++) {
            String[] input = scanner.nextLine().split(" ");
            int N = Integer.parseInt(input[0]);
            int K = Integer.parseInt(input[1]);
            String finalString = scanner.nextLine();
            String originalString = decode(finalString, K);
            System.out.println(originalString);
        }
    }
    private static String decode(String s, int K) {
        char[] chars = s.toCharArray();
        for (int i = K; i >= 1; i--) {
            reverse(chars, 0, i - 1);
        }
        return new String(chars);
    }
    private static void reverse(char[] chars, int start, int end) {
        while (start < end) {
            char temp = chars[start];
            chars[start] = chars[end];
            chars[end] = temp;
            start++;
            end--;
        }
    }
}
