import java.util.Scanner;
public class MinimumScaleLength {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] lengths = new int[n];
        for (int i = 0; i < n; i++) {
            lengths[i] = scanner.nextInt();
        }
        int maxScaleLength = lengths[0];
        for (int i = 1; i < n; i++) {
            maxScaleLength = gcd(maxScaleLength, lengths[i]);
        }
        System.out.println(maxScaleLength);
    }
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
