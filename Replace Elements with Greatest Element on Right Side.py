import java.util.Scanner;
public class ReplaceElements {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        replaceElements(arr);
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
    public static void replaceElements(int[] arr) {
        int n = arr.length;
        int maxRight = -1; 
        for (int i = n - 1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = maxRight;
            maxRight = Math.max(maxRight, temp);
        }
    }
}