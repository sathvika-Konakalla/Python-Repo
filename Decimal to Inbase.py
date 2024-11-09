import java.util.Scanner;
public class DecimalToInbase {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int innum = scanner.nextInt();
        int inbase = scanner.nextInt();
        int maxZeros = -1;
        int currentZeros = 0;
        while (innum > 0) {
            int remainder = innum % inbase;
            innum /= inbase;

            if (remainder == 0) {
                currentZeros++;
                maxZeros = Math.max(maxZeros, currentZeros);
            } else {
                currentZeros = 0;
            }
        }
        System.out.println(maxZeros);
    }
}