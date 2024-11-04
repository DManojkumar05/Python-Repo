import java.util.*;
public class main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int y=sc.nextInt();
        int res=y%100;
        System.out.printf("%02d\n",res);
    }
}