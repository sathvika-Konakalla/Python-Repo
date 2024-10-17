import java.util.Scanner;
public class ValueSameAsCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int count = 0;
        int[] frequency = new int[10]; 
        for (int element : arr) {
            frequency[element]++;
        }
        for (int i = 1; i <= 9; i++) {
            if (frequency[i] == i) {
                count++;
            }
        }
        System.out.println(count);
    }
}