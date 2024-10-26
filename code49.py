import java.util.Scanner;
public class StringGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String result = reduceString(input);
        System.out.println(result);     
        scanner.close();
    }
    private static String reduceString(String str) {
        StringBuilder sb = new StringBuilder();
        for (char ch : str.toCharArray()) {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == ch) {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(ch);
            }
        }
        return sb.length() == 0 ? "-1" : sb.toString();
    }
}
