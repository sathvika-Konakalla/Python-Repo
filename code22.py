import java.util.Scanner;
public class MinimumBetweenAandB {
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
        Integer min = null; 
        for (int value : array) {
            if (value >= A && value <= B) {
                if (min == null || value < min) {
                    min = value;
                }
            }
        }
        if (min != null) {
            System.out.println(min);
        } else {
            System.out.println(-1);
        }
    }
}
