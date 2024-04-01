import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int T = sc.nextInt();
        int arr[] = new int[T];


        for (int i = 0; i< T; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            arr[i] = x + y;
        }
        for (int k : arr) {
            System.out.println(k);
        }
    }
}