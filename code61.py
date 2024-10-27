import java.util.Scanner;
public class CountCharacters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.nextLine();
        int vowelCount = 0;
        int consonantCount = 0;
        int digitCount = 0;
        int spaceCount = 0;
        String vowels = "aeiouAEIOU";
        for (char ch : S.toCharArray()) {
            if (Character.isWhitespace(ch)) {
                spaceCount++;
            } else if (Character.isDigit(ch)) {
                digitCount++;
            } else if (Character.isLetter(ch)) {
                if (vowels.indexOf(ch) != -1) {
                    vowelCount++;
                } else {
                    consonantCount++;
                }
            }
        }
        
        System.out.println("Vowels: " + vowelCount);
        System.out.println("Consonants: " + consonantCount);
        System.out.println("Digits: " + digitCount);
        System.out.println("White spaces: " + spaceCount);
    }
}
