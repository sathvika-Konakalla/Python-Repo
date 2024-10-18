import java.util.Scanner;
public class MinAbsDiff {
    public static int minAbsDiff(int N) {
        int powerOfTwo = 1;
        while (powerOfTwo < N) {
            powerOfTwo *= 2;
        }
        return Math.min(Math.abs(N - powerOfTwo), Math.abs(N - powerOfTwo / 2));
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int result = minAbsDiff(N);
        System.out.println(result);
    }
}