

// >>>>>>>>>>>>>>>>>>>>> reverse an array <<<<<<<<<<<<<<<<<

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, *arr2;
    scanf("%d", &num);

    arr = (int*) malloc(num * sizeof(int));
    arr2 = (int*) malloc(num * sizeof(int));

    for(int i = 0, j = num - 1; i < num; i++, j--){
        scanf("%d", &arr[i]);
        arr2[j] = arr[i];
    }

    arr = arr2;
    for(int i = 0; i < num; i++){
        printf("%d ",arr[i]);
    }

    free(arr);
    free(arr2);

    return 0;
}


// >>>>>>>>>> print some stuff <<<<<<<<<<

#include <stdio.h>

int main()
{

    char ch;
    char s[100], sen[100];

    scanf("%c", &ch);
    scanf("%s", &s);
    scanf(" %[^\n]", sen);  // very important

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);

    return 0;
}
