import java.util.Scanner;
public class TotalMoney {
    public static long calculateTotalMoney(int D, int d, int P, int Q) {
        long totalMoney = 0;
        int intervals = D / d;
        int remainingDays = D % d;
        for (int i = 0; i < intervals; i++) {
            int daysInInterval = d;
            long dailyRate = P + i * Q;
            totalMoney += dailyRate * daysInInterval;
        }
        long dailyRate = P + intervals * Q;
        totalMoney += dailyRate * remainingDays;
        return totalMoney;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int D = scanner.nextInt();
            int d = scanner.nextInt();
            int P = scanner.nextInt();
            int Q = scanner.nextInt();
            long totalMoney = calculateTotalMoney(D, d, P, Q);
            System.out.println(totalMoney);
        }
    }
}