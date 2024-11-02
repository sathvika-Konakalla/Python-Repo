import java.util.Scanner;
public class ClosestPrimeDifference {
    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        if (num <= 3) return true;
        if (num % 2 == 0 || num % 3 == 0) return false;
        for (int i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) return false;
        }
        return true;
    }
    public static int closestPrimeDifference(int N) {
        if (isPrime(N)) {
            return 0;
        }
        int higherPrime = N + 1;
        while (!isPrime(higherPrime)) {
            higherPrime++;
        }
        int lowerPrime = N - 1;
        while (lowerPrime > 1 && !isPrime(lowerPrime)) {
            lowerPrime--;
        }
        int diffHigher = Math.abs(higherPrime - N);
        int diffLower = (lowerPrime > 1) ? Math.abs(lowerPrime - N) : Integer.MAX_VALUE;
        return Math.min(diffHigher, diffLower);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int result = closestPrimeDifference(N);
        System.out.println(result);
    }
}
