import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();

        int sum = 0;
        int min = 0;

        for (int i = 1; i * i <= n; i++) {
            if (i * i >= m) { // 제곱수가 m 보다 크면 더함
                sum += i * i;
                if (min == 0) {
                    min = i * i;
                }
            }
        }
        if (sum == 0) {
            System.out.println("-1");
        }else {
            System.out.println(sum);
            System.out.println(min);

        }
    }
}


