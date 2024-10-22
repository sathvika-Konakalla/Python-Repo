import java.util.Scanner;
public class MaximumSubarray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = scanner.nextInt();
        }
        int maxSoFar = nums[0];
        int maxEndingHere = nums[0];
        for (int i = 1; i < N; i++) {
            maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        System.out.println(maxSoFar);
    }
}
