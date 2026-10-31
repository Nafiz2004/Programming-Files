import numpy as np

#the number of test cases.
t = int(input())

# Size of the array(n) and the number of queries(q)
n,q = map(int, input().split())

#ELEMENSTS OF ARRAY(n)
n = np.array(eval(input()))

#description of a query.
l, r, m = map(int, input().split())

#  Couple:
t = int(input())

for i in range(t):
    n,q = map(int, input().split())
    n = list(map(int, input().split()))
    for k in range(q):
        l, r, m = map(int, input().split())


# stuck in the middle
def count(word, letter):
    counter = 0
    for i in word:
        if i == letter:
            counter+=1
    return counter

Test = int(input())
for i in range(Test):
    length = int(input())
    string = input()[:length]

    mid_pos = int((length+1)/2)
    mid_letter = string[mid_pos-1]
    mid_letter_count = count(string, mid_letter)

    if mid_letter_count > (length / 2):
        print("YES")
    else:
        print("NO")



#include<stdio.h>

int counter(char word, int letter){
  int count = 0;
  for(int i, i < strlen(word), i++){
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
  for(int i, i <= Test, i++){
    scanf("%d", &length);
    char string[length];
    scanf("%s", string);

    mid_pos = int((length+1)/2);
    mid_letter = string[mid_pos-1];
    mid_letter_count = counter(string, mid_letter);

    if (mid_letter_count > (length / 2)){
        printf("YES");
      }
    else{
        printf("NO");
      }
  }

}
