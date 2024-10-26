import java.util.Scanner;
public class LuckyCharacter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        char luckyLetter = input.charAt(6);
        System.out.println(luckyLetter);
    }
}
