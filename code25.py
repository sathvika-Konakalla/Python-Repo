import java.util.Scanner;
public class PredictTheWinner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = scanner.nextInt();
        }
        int totalSum = 0;
        for (int number : numbers) {
            totalSum += number;
        }
        if (totalSum % 4 == 0)
            System.out.println("X");
        else 
            System.out.println("Y");
    }
}
