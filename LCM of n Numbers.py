import java.util.Scanner;
public class LCMOfArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        long lcm = 1; 
        for (int element : nums) {
            lcm = lcm(lcm, element); 
        }
        System.out.println(lcm);
    }
    public static long lcm(long a, long b) {
        return a * (b / gcd(a, b));
    }
    public static long gcd(long a, long b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}