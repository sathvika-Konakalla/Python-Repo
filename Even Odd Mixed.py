import java.util.Scanner;
public class EvenOddMixed {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean isEven = true;
        boolean isOdd = true;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 == 0) {
                isOdd = false;
            } else {
                isEven = false;
            }
            n /= 10;
        }
        if (isEven) {
            System.out.println("Even");
        } else if (isOdd) {
            System.out.println("Odd");
        } else {
            System.out.println("Mixed");
        }
    }
}