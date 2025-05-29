
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine(); // 현재 시간
        String b= sc.nextLine(); // 종료 시간
        String[] x = a.split(":"); //배열로 저장
        String[] y = b.split(":");
        int hour = Integer.parseInt(y[0]) - Integer.parseInt(x[0]) + 23;
        int min = Integer.parseInt(y[1]) - Integer.parseInt(x[1]) + 59;
        int sec = Integer.parseInt(y[2]) - Integer.parseInt(x[2]) + 60;
        if (sec >= 60) {
            sec -= 60;
            min += 1;
        }
        if (min >= 60) {
            min -= 60;
            hour += 1;
        }
        if (hour >= 24) {
            hour -= 24;
        }
        System.out.format("%02d:%02d:%02d", hour, min, sec);


    }
}
