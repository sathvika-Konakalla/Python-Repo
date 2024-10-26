import java.util.Scanner;
public class Marathon {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt(); 
        int b = scanner.nextInt(); 
        int c = scanner.nextInt(); 
        int d = scanner.nextInt(); 
        int count = 0;
        if (b > a) count++;
        if (c > a) count++;
        if (d > a) count++;
        System.out.println(count);
    }
}
