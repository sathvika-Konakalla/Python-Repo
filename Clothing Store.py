import java.util.HashMap;
import java.util.Scanner;

public class ClothingStore {

    public static int countSockPairs(int[] socks) {
        HashMap<Integer, Integer> sockCounts = new HashMap<>();
        for (int sock : socks) {
            sockCounts.put(sock, sockCounts.getOrDefault(sock, 0) + 1);
        }

        int pairs = 0;
        for (int count : sockCounts.values()) {
            pairs += count / 2;
        }

        return pairs;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] socks = new int[N];

        for (int i = 0; i < N; i++) {
            socks[i] = scanner.nextInt();
        }

        int pairs = countSockPairs(socks);
        System.out.println(pairs);
    }
}