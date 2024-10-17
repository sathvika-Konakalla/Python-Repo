import java.util.Scanner;
public class ElementsNotInBetweenAB {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int count = 0;
        boolean found = false;
        for (int element : arr) {
            if (element < a || element > b) {
                count++;
                found = true;
                System.out.print(element + " ");
            }
        }
        if (!found) 
            System.out.println("-1"); 
    }
}