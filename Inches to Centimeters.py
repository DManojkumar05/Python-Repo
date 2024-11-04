import java.util.Scanner;
public class main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int h=sc.nextInt();
        double res=h*2.54;
        System.out.printf("%.2f",res);
    }
}