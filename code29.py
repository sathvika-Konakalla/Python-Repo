import java.util.HashMap;
import java.util.Scanner;
public class ElementAndCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = scanner.nextInt();
        }
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        for (int num : nums) {
            if (countMap.containsKey(num)) {
                System.out.print(num + " " + countMap.get(num) + " ");
                countMap.remove(num); 
            }
        }
        System.out.println();
    }
}
