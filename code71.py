import java.util.Scanner;
public class CircularPrime {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        if (isPrime(N)) {
            int reversedN = reverseNumber(N);
            if (isPrime(reversedN)) {
                System.out.println("circular prime");
            } else {
                System.out.println("prime but not a circular prime");
            }
        } else {
            System.out.println("not prime");
        }
    }
    private static boolean isPrime(int number) {
        if (number <= 1) return false; 
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
    private static int reverseNumber(int number) {
        int reversed = 0;
        while (number > 0) {
            reversed = reversed * 10 + number % 10;
            number /= 10;
        }
        return reversed;
    }
}
