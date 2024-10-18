import java.util.Scanner;
public class CountEvenNumbersBetweenOdd {
    public static int countEvenNumbers(int[] arr) {
        int count = 0;
        boolean foundOdd = false;
        for (int num : arr) {
            if (num % 2 != 0) {  
                foundOdd = true;
            } else if (foundOdd && num % 2 == 0) {  
                count++;
                foundOdd = false;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        int evenCount = countEvenNumbers(arr);
        System.out.println(evenCount);
    }
}