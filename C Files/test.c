
#include <stdio.h>
#include <conio.h>

int main() {
    int num, reversed_num = 0, original_num;

    printf("Enter a number: ");
    scanf("%d", &num);

    original_num = num;
    if (original_num < 0) num = -num;

    while(num != 0){
        reversed_num = reversed_num * 10 + num % 10;
        num /= 10;
    }

    if (original_num < 0) reversed_num = -reversed_num
    printf("Reverse of %d is %d\n", original_num, reversed_num);
    getch();
    return 0;
}
