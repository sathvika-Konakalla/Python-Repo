import java.util.Scanner;
public class EdgeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        if (areConnected(a, b)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
    public static boolean areConnected(int a, int b) {
        return Math.abs(a - b) == 1 || (a == 1 && b == 10) || (a == 10 && b == 1);
    }
}
