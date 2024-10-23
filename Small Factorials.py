import java.util.Scanner;
public class SmallFactorials {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            long factorial = calculateFactorial(n);
            System.out.println(factorial);
        }
    }
    public static long calculateFactorial(int n) {
        if (n == 0 || n == 1) return 1;
        else  return n * calculateFactorial(n - 1);
    }
}