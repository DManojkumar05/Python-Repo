import java.util.Scanner;
public class CircleArea {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int R = scanner.nextInt();
        double area = 3.14*R*R;
        System.out.printf("%.2f%n", area);
    }
}