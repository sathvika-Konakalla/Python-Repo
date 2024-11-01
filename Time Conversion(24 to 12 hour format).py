import java.util.Scanner;
public class TimeConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String time24 = scanner.nextLine();
        String[] parts = time24.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        String period;
        if (hours >= 12) {
            period = "PM";
        } else {
            period = "AM";
        }
        if (hours == 0) {
            hours = 12; 
        } else if (hours > 12) {
            hours -= 12; 
        }
        String time12 = String.format("%02d:%02d %s", hours, minutes, period);
        System.out.println(time12);
    }
}
