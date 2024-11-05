import java.util.Scanner;
public class HarshadNumber {
    public static boolean isHarshadNumber(int N) {
        int sumOfDigits = 0;
        int originalNumber = N;
        while (N > 0) {
            sumOfDigits += N % 10;
            N /= 10;
        }
        return originalNumber % sumOfDigits == 0;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        if (isHarshadNumber(N)) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}