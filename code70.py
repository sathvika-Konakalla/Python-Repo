import java.util.Scanner;
public class TimeConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalSeconds = scanner.nextInt();
        int hours = totalSeconds / 3600; 
        int minutes = (totalSeconds % 3600) / 60; 
        int seconds = totalSeconds % 60; 
        System.out.printf("H:M:S-%d:%d:%d%n", hours, minutes, seconds);
    }
}
