import java.util.Scanner;
public class PrintTable {
    public static void printTable(int N, int R) {
        for (int i = 1; i <= R; i += 2) {
            int product = N * i;
            System.out.println(N + " x " + i + " = " + product);
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int R = scanner.nextInt();
        printTable(N, R);
    }
}