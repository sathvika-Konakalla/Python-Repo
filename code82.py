import java.util.Scanner;

public class DistinctBinaryStrings {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt();
            String s = scanner.next();

            int count = 0;
            for (int i = 0; i < n; i++) {
                if (i == 0 || s.charAt(i) != s.charAt(i - 1)) {
                    count++;
                }
            }
            System.out.println(count);
        }
    }
}