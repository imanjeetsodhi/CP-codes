// read a number check the number is divisible by 7 or last digit is 5 

import java.util.Scanner;

public class divisibleBySeven{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number : ");
        int num = sc.nextInt();
        if(num %  7 == 0){
            if(num % 10 == 5){
               System.out.println("number is divisible by 7 and last digit is 5"); 
            }
            
        }else{
            System.out.println("number is not divisible by 7 and last digit is 4");
        }
        sc.close();
    }
}
