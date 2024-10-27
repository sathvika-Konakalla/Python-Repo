import java.util.Scanner;
public class WordCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine();
        int wordCount = countWords(inputString);
        System.out.println(wordCount);
    }
    public static int countWords(String s) {
        String[] words = s.trim().split("\\s+");
        return words.length == 1 && words[0].isEmpty() ? 0 : words.length; 
    }
}
