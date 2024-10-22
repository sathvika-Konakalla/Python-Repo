import java.util.Scanner;
public class SumBetweenAandB {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] array = new int[N];
        for (int i = 0; i < N; i++) {
            array[i] = scanner.nextInt();
        }
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        if (A > B) {
            int temp = A;
            A = B;
            B = temp;
        }
        int sum = 0;
        boolean found = false; 
        for (int value : array) {
            if (value >= A && value <= B) {
                sum += value;
                found = true;
            }
        }
        System.out.println(found ? sum : 0); 
    }
}
