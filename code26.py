import java.util.Scanner;
public class GreatestNumberOfCandies {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] candies = new int[N];
        for (int i = 0; i < N; i++) {
            candies[i] = scanner.nextInt();
        }
        int extraCandies = scanner.nextInt();
        int maxCandies = 0;
        for (int candy : candies) {
            maxCandies = Math.max(maxCandies, candy);
        }
        String[] result = new String[N];
        for (int i = 0; i < N; i++) {
            result[i] = (candies[i] + extraCandies >= maxCandies) ? "True" : "False";
        }
        for (int i = 0; i < N; i++) {
            System.out.print(result[i]);
            if (i < N - 1) {
                System.out.print(" ");
            }
        }
    }
}
