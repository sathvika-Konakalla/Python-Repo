import java.util.Scanner;
public class ElementsSmallerThanAverage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
            sum += arr[i];
        }
        int average = sum / n;
        int count = 0;
        for (int element : arr) {
            if (element <= average) 
                count++;
        }
        System.out.println(count);
    }
}