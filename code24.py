import java.util.Scanner;
public class CountDivisibleElements {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        int count = 0;
        for (int i = 0; i < N; i++) {
            int element = scanner.nextInt();
            if (element % K == 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
