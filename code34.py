import java.util.Scanner;
public class SankarAndMaths {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int distinctCount = (N + 1) / 2;
        System.out.println(distinctCount);
    }
}
