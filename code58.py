import java.util.Scanner;
public class BalancedStringSplitter {
    public static int balancedStringSplit(String s) {
        int balanceCount = 0; 
        int splitCount = 0;   
        for (char c : s.toCharArray()) {
            if (c == 'L') {
                balanceCount++;
            } else if (c == 'R') {
                balanceCount--;
            }
            if (balanceCount == 0) {
                splitCount++;
            }
        }
        return splitCount;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine().trim();
        int result = balancedStringSplit(inputString);
        System.out.println(result);
        scanner.close();
    }
}
