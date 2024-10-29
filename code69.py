import java.util.Scanner;
public class CountSubstringsWithOnes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); 
        while (T-- > 0) {
            int N = scanner.nextInt(); 
            String S = scanner.next(); 
            int countOnes = 0;
            for (char c : S.toCharArray()) {
                if (c == '1') {
                    countOnes++;
                }
            }
            int numSubstrings = (countOnes * (countOnes + 1)) / 2;
            System.out.println(numSubstrings);
        }
    }
}
