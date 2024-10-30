import java.util.Scanner;
public class BestTimeToBuyAndSellStockII {
    public static int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i + 1] > prices[i]) {
                profit += prices[i + 1] - prices[i];
            }
        }
        return profit;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();
        int[] prices = new int[size];
        for (int i = 0; i < size; i++) {
            prices[i] = scanner.nextInt();
        }
        int result = maxProfit(prices);
        System.out.println(result);
    }
}
