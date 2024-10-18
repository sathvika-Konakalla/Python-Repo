import java.util.Scanner;
public class HCFofArray {
    public static int findHCF(int[] arr) {
        int hcf = arr[0];
        for (int i = 1; i < arr.length; i++) {
            hcf = findGCD(hcf, arr[i]);
        }
        return hcf;
    }
    public static int findGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return findGCD(b, a % b);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        int hcf = findHCF(arr);
        System.out.println(hcf);
    }
}