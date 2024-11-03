import java.util.Scanner;
public class TeamSelection {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int[] participationCounts = new int[n];
        for (int i = 0; i < n; i++) {
            participationCounts[i] = scanner.nextInt();
        }
        int eligibleCount = 0;
        for (int i = 0; i < n; i++) {
            if (5 - participationCounts[i] >= k) {
                eligibleCount++;
            }
        }
        int maxTeams = eligibleCount / 3;
        System.out.println(maxTeams);
    }
}
