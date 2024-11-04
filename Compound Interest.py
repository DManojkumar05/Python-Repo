import java.util.*;
public class main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        double p=sc.nextInt();
        double r=sc.nextInt();
        double t=sc.nextInt();
        double a=p*Math.pow((1+r/100),t);
        double c=a-p;
        System.out.printf("%.2f\n",c);
    }
}