import java.util.Scanner;
public class DescendingArray {
    public static boolean isDescending(int[] arr) {
        if (arr.length < 2) {
            return true;
        }
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] >= arr[i - 1]) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        if (isDescending(arr)) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}