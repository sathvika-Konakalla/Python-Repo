import java.util.Scanner;
public class TimeConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String time12Hour = scanner.nextLine();
        String time24Hour = convertTo24HourFormat(time12Hour);
        System.out.println(time24Hour);
    }
    public static String convertTo24HourFormat(String time12) {
        String[] parts = time12.split(" ");
        String time = parts[0]; 
        String period = parts[1]; 
        String[] timeParts = time.split(":");
        int hours = Integer.parseInt(timeParts[0]);
        String minutes = timeParts[1];
        if (period.equals("PM") && hours != 12) {
            hours += 12;
        } else if (period.equals("AM") && hours == 12) {
            hours = 0; 
        }
        String hours24 = String.format("%02d", hours);
        return hours24 + ":" + minutes;
    }
}
