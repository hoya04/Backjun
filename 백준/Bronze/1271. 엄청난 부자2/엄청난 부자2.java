import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        BigInteger M = scanner.nextBigInteger();
        BigInteger N = scanner.nextBigInteger();
        System.out.println(M.divide(N));
        System.out.println(M.remainder(N));

    }
}
