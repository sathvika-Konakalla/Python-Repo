import java.util.Scanner;
public class ArrayRotation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        while (T-- > 0) {
            int N = scanner.nextInt();
            int K = scanner.nextInt();
            int[] A = new int[N];
            for (int i = 0; i < N; i++) {
                A[i] = scanner.nextInt();
            }
            K = K % N;
            if (K != 0) {
                int[] rotatedArray = new int[N];
                for (int i = 0; i < N; i++) {
                    rotatedArray[(i + K) % N] = A[i];
                }
                for (int i = 0; i < N; i++) {
                    System.out.print(rotatedArray[i]);
                    if (i < N - 1) {
                        System.out.print(" ");
                    }
                }
            } else {
                for (int i = 0; i < N; i++) {
                    System.out.print(A[i]);
                    if (i < N - 1) {
                        System.out.print(" ");
                    }
                }
            }
            System.out.println(); 
        }
    }
}
