import java.util.Scanner;
public class EvenNumberOfDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = scanner.nextInt();
        }
        int evenDigitCount = 0;
        for (int num : nums) {
            if (String.valueOf(num).length() % 2 == 0) {
                evenDigitCount++;
            }
        }
        System.out.println(evenDigitCount);
    }
}
