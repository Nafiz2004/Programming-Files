
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

    for i in range(1,length-1,2):
        k = 0
        mid_pos = int((i+1)/2)
        mid_letter = string[k,i+1][mid_pos-1]
        mid_letter_count = count(string[k,i+1], mid_letter)

        if mid_letter_count > (length / 2):
            print("YES")
        else:
            print("NO")
