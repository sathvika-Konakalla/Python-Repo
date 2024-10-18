import java.util.HashSet;
import java.util.Scanner;
public class UniqueEvenCount {
    public static int countUniqueEven(int[] arr) {
        HashSet<Integer> uniqueEven = new HashSet<>();
        for (int num : arr) {
            if (num % 2 == 0) {
                uniqueEven.add(num);
            }
        }
        return uniqueEven.size();
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        int uniqueEvenCount = countUniqueEven(arr);
        System.out.println(uniqueEvenCount);
    }
}