import java.util.HashMap;
import java.util.ArrayList;
import java.util.Scanner;
public class NTimesRepeatedElements {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] array = new int[N];
        for (int i = 0; i < N; i++) {
            array[i] = scanner.nextInt();
        }
        int K = scanner.nextInt();
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : array) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        ArrayList<Integer> result = new ArrayList<>();
        for (int key : countMap.keySet()) {
            if (countMap.get(key) == K) {
                result.add(key);
            }
        }
        if (result.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int num : result) {
                System.out.print(num + " ");
            }
        }
    }
}
