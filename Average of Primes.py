import java.util.Scanner;
public class AverageOfPrimes {
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        if (num <= 3) {
            return true;
        }
        if (num % 2 == 0 || num % 3 == 0) {
            return false;
        }
        int i = 5;
        while (i * i <= num) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }
        return true;
    }
    public static double averageOfPrimes(int[] arr) {
        int primeSum = 0;
        int primeCount = 0;
        for (int num : arr) {
            if (isPrime(num)) {
                primeSum += num;
                primeCount++;
            }
        }
        if (primeCount == 0) {
            return 0;
        }
        return (double) primeSum / primeCount;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        double average = averageOfPrimes(arr);
        System.out.printf("%.2f", average);
    }
}