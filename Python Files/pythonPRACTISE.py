

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
