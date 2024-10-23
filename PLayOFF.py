import java.util.Scanner;
public class Playoff {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int winner = findWinner(n);
            System.out.println(winner);
        }
    }
    public static int findWinner(int n) {
        return (int) Math.pow(2, n) - 1;
    }
}