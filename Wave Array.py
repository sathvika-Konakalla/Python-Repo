import java.util.Scanner;
public class SineWaveArray {
    public static boolean isSineWave(int[] arr) {
        if (arr.length < 3) {
            return false;
        }
        boolean increasing = arr[1] > arr[0];
        for (int i = 1; i < arr.length - 1; i++) {
            if (increasing) {
                if (arr[i] > arr[i + 1]) {
                    increasing = false;
                } else if (arr[i] < arr[i + 1]) {
                    return false;
                }
            } else {
                if (arr[i] < arr[i + 1]) {
                    increasing = true;
                } else if (arr[i] > arr[i + 1]) {
                    return false;
                }
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        if (isSineWave(arr)) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}