import java.util.Scanner;
import java.util.HashMap;
public class UniqueMaximumNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int maxUniqueNum = findMaxUniqueNum(arr);
        System.out.println(maxUniqueNum);
    }
    public static int findMaxUniqueNum(int[] arr) {
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : arr) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        int maxUniqueNum = -1;
        for (int num : arr) {
            if (frequencyMap.get(num) == 1 && num > maxUniqueNum)
                maxUniqueNum = num;
        return maxUniqueNum;
    }
}
}