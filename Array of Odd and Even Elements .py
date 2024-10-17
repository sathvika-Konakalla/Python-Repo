import java.util.ArrayList;
import java.util.Scanner;
public class OddEvenElementsArray {
    public static int[] separateOddEven(int[] arr) {
        ArrayList<Integer> oddList = new ArrayList<>();
        ArrayList<Integer> evenList = new ArrayList<>();
        for (int element : arr) {
            if (element % 2 != 0) oddList.add(element);
            else  evenList.add(element);
            
        }
        int[] combinedArray = new int[oddList.size() + evenList.size()];
        int index = 0;
        for (int odd : oddList) {
            combinedArray[index++] = odd;
        }
        for (int even : evenList) {
            combinedArray[index++] = even;
        }
        return combinedArray;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int[] result = separateOddEven(arr);
        for (int element : result) {
            System.out.print(element + " ");
        }
    }
}