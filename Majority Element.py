import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class MajorityElement {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int majorityElement = findMajorityElement(arr);
        System.out.println(majorityElement);
    }
    public static int findMajorityElement(int[] arr) {
        Map<Integer, Integer> countMap = new HashMap<>();
        int majorityCount = arr.length / 2;
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            if (countMap.get(num) > majorityCount) {
                return num; 
            }
        }
        return -1; 
    }
}
