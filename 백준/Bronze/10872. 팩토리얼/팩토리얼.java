import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int result = 1;
        int N = sc.nextInt();

      for (int i = N; i >0; i--) {
          result *= i;

        }
        System.out.println(result);
    }
}
