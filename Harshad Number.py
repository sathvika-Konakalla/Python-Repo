import java.util.Scanner;
public class HarshadNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int N = scanner.nextInt();
            int sumOfDigits = sumDigits(N);
            if (N % sumOfDigits == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
    private static int sumDigits(int number) {
        int sum = 0;
        
        while (number > 0) {
            sum += number % 10; 
            number /= 10;       
        }
        return sum;
    }
}
