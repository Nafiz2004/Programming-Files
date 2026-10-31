#include<stdio.h>
#include<string.h>

int counter(char word[], int letter){
  int count = 0;
  for(int i=0; i < strlen(word); i++){
    if(word[i] == letter){
      count++;
    }
  }
  return count;
}

int main(){
  int Test, length, mid_pos, mid_letter_count;
  char mid_letter;

  scanf("%d", &Test);
  for(int i=1; i <= Test; i++){
    scanf("%d", &length);
    char string[length];
    scanf("%s", string);

    mid_pos = (length+1)/2;
    mid_letter = string[mid_pos-1];
    mid_letter_count = counter(string, mid_letter);

    if (mid_letter_count > (length / 2)){
        printf("YES\n");
      }
    else{
        printf("NO\n");
      }
  }

}
