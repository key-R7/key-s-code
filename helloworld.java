import java.util.Scanner;

public class helloworld {
        public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in);
                if (!scanner.hasNextDouble()) {
                        scanner.close();
                        return;
                }

                double f = scanner.nextDouble();
                scanner.close();
                double c = 5 * (f - 50) / 9 + 10;
                System.out.printf("The temperature is %.2f.%n", c);
        }
}
