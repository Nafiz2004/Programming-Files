

############# print highest sum of a person ############
n = int(input())
student_marks = {}
var = 0
allias = None

for _ in range(n):
    name, *marks = input().split()
    marks = list(map(float, marks))
    student_marks[name] = marks

    if(sum(marks) > var):
        var = sum(marks)
        allias = name

print(allias, var)



################## print average of a given person #############

n = int(input())
student_marks = {}

for _ in range(n):
    name, *marks = input().split()
    marks = list(map(float, marks))
    student_marks[name] = marks

query_name = input()
avg_score = sum(student_marks[query_name]) / 3
print("%0.2f" %avg_score)


################ nested list #########

nums = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

        lst = [name, score]
        nums.append(lst)

nums.sort(key = lambda a : a[1], reverse =True)
print(nums)

last_val = nums[-1][1]
while (nums[-1][1] == last_val):
    nums.pop()
print(nums)
last_real_val = nums[-1][1]
store = []
for i in range(len(nums)):
    if nums[i][1] == last_real_val:
        store.append(nums[i][0])

store.sort()
for j in store:
    print(j)


################ factorial #############

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

print(fact(10))

############# dictionay ################

n = int(input())

d = dict()
for i in range(1, n+1):
    d[i] = i * i
print(d)


###########
lst = list(map(int, input().split(",")))
print(lst)
tple=tuple(lst)
print(tple)

lst2 = list(eval(input()))
print(lst2)

for i in lst2:
    print(f"{i} -> {type(i)}")

## safe oftion
import ast
lst2 = list(ast.literal_eval(input()))
print(lst2)

###################
# Question 5
# Question: Define a class which has at least two methods:
# getString: to get a string from console input printString:
# to print the string in upper case. Also please include simple
# test function to test the class methods.


class basic_func:
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())

obj = basic_func()
obj.getString()
obj.printString()


class basic_operation:
    def getString(self,str):
        return str
    def printString(self,value):
        print(value)

obj2 = basic_operation()

val = obj2.getString("Nafiz")
obj2.printString(val)
