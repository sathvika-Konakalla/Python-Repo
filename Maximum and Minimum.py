import java.util.HashMap;
import java.util.Scanner;
public class MaximumAndMinimum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        boolean found = false;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (int element : arr) {
            frequencyMap.put(element, frequencyMap.getOrDefault(element, 0) + 1);
        }
        for (int element : arr) {
            if (frequencyMap.get(element) == element && element != 0) {
                if (element < min) {
                    min = element;
                }
                if (element > max) {
                    max = element;
                }
                found = true;
            }
        }
        if (!found) {
            System.out.println("-1");
        } else {
            System.out.println(min + " " + max);
        }
    }
}