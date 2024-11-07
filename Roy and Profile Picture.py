import java.util.Scanner;
public class RoyAndProfilePicture {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int L = scanner.nextInt();
        int N = scanner.nextInt();
        for (int i = 0; i < N; i++) {
            int W = scanner.nextInt(); 
            int H = scanner.nextInt(); 
            if (W < L || H < L) {
                System.out.println("UPLOAD ANOTHER");
            }
            else if (W == H) {
                System.out.println("ACCEPTED");
            }
            else {
                System.out.println("CROP IT");
            }
        }
    }
}
