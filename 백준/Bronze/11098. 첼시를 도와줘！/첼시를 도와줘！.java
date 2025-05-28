import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // 테스트 케이스 개수
        for (int i = 0; i < n; i++) {
            int p = scanner.nextInt();// 고려해야할 선수의 수
            scanner.nextLine();
            int maxSalary = 0; // 가장 높은 급여
            String bestPlayer = "";
            for (int j = 0; j < p; j++) {
                int salary = scanner.nextInt();
                String name = scanner.next();

                if (salary > maxSalary) {
                    maxSalary = salary;
                   bestPlayer = name;
                }
            }
            System.out.println(bestPlayer);
        }
    }
}
