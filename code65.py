import java.util.Scanner;
public class FindTheHomeless {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] people = new int[N];
        int[] houses = new int[N];
        for (int i = 0; i < N; i++) {
            people[i] = scanner.nextInt();
        }
        for (int i = 0; i < N; i++) {
            houses[i] = scanner.nextInt();
        }
        int unassignedCount = 0;
        boolean[] houseOccupied = new boolean[N]; 
        for (int i = 0; i < N; i++) {
            boolean assigned = false;
            for (int j = 0; j < N; j++) {
                if (!houseOccupied[j] && houses[j] >= people[i]) {
                    houseOccupied[j] = true; 
                    assigned = true;
                    break; 
                }
            }
            if (!assigned) {
                unassignedCount++;
            }
        }
        System.out.println(unassignedCount);
    }
}
