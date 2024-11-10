import java.util.Scanner;
public class StringRotatedByTwoPlaces {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String a = scanner.nextLine();
        String b = scanner.nextLine();
        int n = a.length();
        if (n != b.length()) {
            System.out.println(0);
            return;
        }
        String rotated1 = a.substring(2) + a.substring(0, 2);
        String rotated2 = a.substring(n - 2) + a.substring(0, n - 2);
        if (rotated1.equals(b) || rotated2.equals(b)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}