import java.util.Scanner;
public class PasswordGenerator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String password = generatePassword(input);
        System.out.println(password);
    }
    private static String generatePassword(String input) {
        StringBuilder password = new StringBuilder();
        String[] entries = input.split(",");
        for (String entry : entries) {
            String[] parts = entry.split(":");
            String name = parts[0];
            String code = parts.length > 1 ? parts[1] : "";
            int maxDigit = -1;
            for (char ch : code.toCharArray()) {
                if (Character.isDigit(ch)) {
                    int digit = Character.getNumericValue(ch);
                    if (digit <= name.length()) {
                        maxDigit = Math.max(maxDigit, digit);
                    }
                }
            }
            if (maxDigit != -1) {
                password.append(name.charAt(maxDigit - 1));
            } else {
                password.append('X');
            }
        }
        return password.toString();
    }
}
