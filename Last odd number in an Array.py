import java.util.Scanner;
public class LastOddNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int lastOddNumber = -1;
        for (int i = 0; i < N; i++) {
            int num = scanner.nextInt();
            if (num % 2 != 0) { 
                lastOddNumber = num;
            }
        }
        System.out.println(lastOddNumber);
    }
}