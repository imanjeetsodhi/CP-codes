// check if a number is divisible by 3 and last digit is 4

import java.util.Scanner;

public class divisibleByThree{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number : ");
        int num = sc.nextInt();
        if(num % 3 == 0){
            if(num % 10 == 4){
                System.out.println("number is divisible by 3 and last digit is 4");
            }
        }else{
            System.out.println("number is not divisible by 3 and last digit is 4");
        }
        sc.close();
    }
}
