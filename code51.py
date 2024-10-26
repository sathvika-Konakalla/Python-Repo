import java.util.Scanner;
public class CompareTwoStrings {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();
        if (s1.equals(s2)) {
            System.out.println("Strings are Equal");
        } else {
            System.out.println("Strings are not Equal");
        }
    }
}
