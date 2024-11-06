import java.util.Scanner;
public class CountWordsInString {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine();
        String[] words = inputString.trim().split("\\s+");
        System.out.println(words.length);
    }
}
