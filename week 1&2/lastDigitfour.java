// // check if last digit of the number is 4 or not 
import java.util.Scanner;

public class lastDigitfour{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number : ");
        int num = sc.nextInt();
        if(num % 10 == 4){
            System.out.print("Last digit is 4");
        }else{
            System.out.print("Last digit is not 4");
        }

        sc.close();
    }
}

