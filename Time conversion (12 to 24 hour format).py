import java.util.Scanner;
public class TimeConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String time12 = scanner.nextLine();
        String[] timeParts = time12.split(":");
        String hours = timeParts[0];
        String minutes = timeParts[1].split(" ")[0];
        String amPm = timeParts[1].split(" ")[1];
        int intHours = Integer.parseInt(hours);
        if (amPm.equalsIgnoreCase("PM") && intHours != 12) {
            intHours += 12;
        } else if (amPm.equalsIgnoreCase("AM") && intHours == 12) {
            intHours = 0;
        }
        String formattedHours = String.format("%02d", intHours);
        String time24 = formattedHours + ":" + minutes;
        System.out.println(time24);
    }
}