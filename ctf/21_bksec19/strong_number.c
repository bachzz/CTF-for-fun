#include <stdio.h>
//#include <conio.h>
//#include <curses.h>


int main(){
    int N, num, temp, digit, factorial, counter, factSum;
     
    //printf("To find all strong numbers between 1 to N");
    //printf("Enter value of N");
    //scanf("%d",&N);
		N = 1000000000;    

    printf("List of strong numbers between 1 to %d\n", N);
    for(num = 1; num <= N; num++){
        /* Calculate sum of factorial of digits of num */
        temp = num;
        factSum = 0;
        while(temp){
           digit = temp%10;   
           /* Calculate factorial of every digit 
            * N! = N*(N-1)*(N-2)*(N-3)*.....*3*2*1 
            */
           for(counter=1, factorial=1; counter<=digit; counter++){
               factorial = factorial * counter;
           }
           factSum += factorial;
           temp = temp/10;
        }
         
        if(factSum == num)
           printf("%d ", num);
    
    }
    //getch();
    return 0;
}
