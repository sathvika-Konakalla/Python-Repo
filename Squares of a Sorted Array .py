import java.util.Scanner;
import java.util.Arrays;
public class SquaresOfSortedArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        int[] squares = new int[n];
        for (int i = 0; i < n; i++) {
            squares[i] = A[i] * A[i];
        }
        Arrays.sort(squares);
        for (int square : squares) {
            System.out.print(square + " ");
        }
    }
}