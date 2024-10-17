import java.util.Scanner;
public class FirstAndLastPair {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int left = 0;
        int right = n - 1;
        while (left < right) {
            System.out.print(arr[left] + " " + arr[right] + " ");
            left++;
            right--;
        }
        if (n % 2 != 0) {
            System.out.print(arr[left] + " 0");
        }
    }
}