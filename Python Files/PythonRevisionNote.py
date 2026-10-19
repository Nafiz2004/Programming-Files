import ast

datas = list(eval(input("Enter: ")))
nums = list(ast.literal_eval(input("Enter: ")))
print(datas)
print(nums)


import math
import matplotlib.pyplot as plt

start, end = map(int, input("Enter starting and ending numbers: ").split())
prime_nums = []

for i in range(start, end + 1):
    if i < 2:
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        prime_nums.append(i)

print(prime_nums)


num = int(input("Enter a number: "))
print(f"Digit of {num} is {len(str(num))}")


def add(num1, num2):
    return num1 + num2

sum = add(10, 20)
print(sum)


def fact(num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i

print(fact(5))

tup = (2, 4, 8, 1, 0)
num = [2, 4, 8, 1, 0]
set = {2, 4, 8, 1, 0}

print(set)

datas = {
    3 : "Nafiz",
    "A" : "Nahid",
    2.5 : ["Mohon", 3, 4.5],
    "Web_Development" : {"Python" : "Django", "JS" : "Node"}
}

print(datas["A"])
print(datas.get(2.5))
print(datas.get(2.5)[0])

datas["ABC"] = "abc"
del datas[3]

print(datas["Web_Development"]["Python"])

j = '* '
for i in range(5):
    print(f"{j*5}")


a, b = 10, 20
b, a = a, b
print(a,b)
a = -a
print(a)

a = 0o123
b = 0x34F
print(oct(a))
print(bin(a))
print(hex(a))
print(bin(b))

print(~12)


num = 10

if num == 1:
    print(num)
elif num < 5:
    print("Bye")
else:
    print("Fuck You")


i = 1
while i <= 5:
    print(i)
    i += 1


num = list(range(1, 11))
print(num)

name = "Nafiz"

for i in name:
    print(i)


for i in range(1, 11):
    print(i)
    break


for i in range(1, 10):
    if i % 2 == 0:
        print("A")
        pass
    print(i)
print("Hi")


statement = f"{"* "*5}\n"*5
print(f"{"* "*5}\n"*5)


for i in range(5):
    for j in range(5):
        print("*", end = " ")
    print()


for i in range(1, 6):
    print(f"{"* " * i}")


for i in reversed(range(1, 6)):
    print(f"{"* " * i}")

j = 5
for i in range(1, 6):
    print(f"{" " * j}{"* " * i}")
    j -= 1


import math
num = 9
for i in range(2, int(math.sqrt(num) + 1)):
    if num % i == 0:
        print("Not a Prime Number")
        break
else:
    print("A prime Number")


import math

start, end = map(int, input("Enter starting and ending value: ").split())
prime_values = []

if start < 2:
for i in range(start, end + 1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break;
    else:
        prime_values.append(i)

print(prime_values)


from array import *

arr = array("i", [7, 3, -2, 8, 1])
arr.append(34)
arr.reverse()
print(arr)


for i in arr:
    print(i, end = " ")


nums = [4, 5, 6, 7, 1]
print(nums)
vals = [i for i in nums]
print(vals)

vals = array("i", [])

for i in range(5):
    x = int(input("Enter: "))
    vals.append(x)

print(vals)

import ast

lst = list(ast.literal_eval(input("Enter: ")))


arr = array("i", lst)
print(arr)


def add(a, b):
    return a+b, b

x, y = add(5, 10)
print(x,y)



def fun(num):
    num = 10
    print(num)

fun(15)


def some_func(name, age = 18):
    print(name, age)

some_func("Nafiz")


def some_func_2(a, *b, c):
    print(a, b, c)

some_func_2(5, 6, 7, c = 5)


def person(name, **data):
    print(name)
    print(type(data))

    print(data["age"])
    print(data.values())
    for i, j in data.items():
        print(i, j)

person(name = "Nafiz", age = 21, batch = "CSE-26", home = "Bogura")


a = 10
def FUNC():
     global a
     a = 15
     print(a, "Inside")

FUNC()
print(a, "Outside")



a, b = 0, 1
print(f"{a}\n{b}")

for i in range(8):
    print(a + b)
    a, b = b, (a + b)



import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())
def iter():
    print("Hello")
    iter()

iter()


def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)


## Lecture-42 -> Lambda

func = lambda num1, num2 : num1 + num2

print(func(5, 10))

## Lecture-43 -> Filter, Map, Reduce

nums = (1,5,2,4,7,6)
evens = list(filter(lambda a : a % 2 == 0, nums))
print(evens)

a, b, c = map(int, input("Enter 3 numbers: ").split())

print(a, b, c)

evens_double = list(map(lambda a : a * 2, evens))
print(evens_double)

from functools import reduce
x = reduce(lambda a, b : a + b, evens_double)
print(x)



## Lecture-44 -> Decorators

def div(a, b):
    print(a / b)

# inner is created to accept x and y when it is called later.
# func refers to the original div function.
# When inner(x, y) is called, it calls func(x, y).
# Since func is the original div(a, b), x is passed to a and y is passed to b.
# return inner returns the inner function object.
# Then: div = div_plugin(div) makes div refer to inner.

def div_plugin(func):
    def mimic(x, y):
        if y > x:
            x, y = y, x
        return func(x, y)
    return mimic

smart_div = div_plugin(div)

div(30, 50)
smart_div(30, 50)

# lecture 45 - module
import test_file


test_file.add(5, 10)
test_file.sub(10, 5)

print(__name__)

# Lecture - 50 --> Object, Class

class Computer:
    def __init__(self):
        print("Init")

    def config(self):
        print("Ryzen-5, 16GB, 512GB-SSD")


com1 = Computer()
print(type(com1))

com1.config()
Computer.config(com1)

#lecture 51
class Computer:

    def __init__(self, cpu, ram, var = None):
        self.cpu = cpu
        self.ram = ram
        self.var = var

    def config(self, battery = "LiOn"):
        print("Config is ", self.cpu, self.ram, end = " ")
        print(battery)

    def update(self, var):
        self.var = value

    def compare(self, other, var):
        if self.var == other.var:
            print("Same")
        else:
            print("Not same")

com1 = Computer("Ryzen-5", 16)
com2 = Computer("i5", 12)

com1.config("Li-pO")
com2.config()

com1.compare(com2, )

com1.update(com1.cpu, "i3")
com1.config()


#lecture 57

class Car:

    wheels = 4
    def __init__(self, name, mil):
        self.name = name
        self.mil = mil

car1 = Car('Ferari', 10)
car2 = Car("BMW", 15)

car1.mil = 8
Car.wheels = 16

print(car1.name, car1.mil, car1.wheels)
print(car2.name, car2.mil, car2.wheels)


#lecture 58

class Student:

    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

    def avg(self):
        print((self.sub1 + self.sub2) / 2)

    @classmethod
    def SchoolName(cls):
        print("ABC School")

    @staticmethod
    def info():
        print("Students are good")

student1 = Student(85, 70)
student1.avg()

Student.SchoolName()

Student.info()



#Lecture 59 -> inner class


class Student:

    def __init__(self, name, roll, cpu, ram):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop(cpu, ram)

    def info(self):
        print(self.name, self.roll)
        print(self.lap.cpu, self.lap.ram)

    class Laptop:

        def __init__(self, cpu, ram):
            self.cpu = cpu
            self.ram = ram

        def info(self):
            print(self.ram, self.cpu)

student1 = Student("Nafiz", 2602014, "i5", 16)
student1.info()

#### Outside Creation of Object of Laptop ####
# lap1 = Student.Laptop("i5", 16)
# lap1.info()


# lecture 60---> inheritence

class A:
    def feature1(self):
        print("Feature 1 is working")

# B is Sub class of A so B inherites everything of A
class B(A):
    def feature2(self):
        print("Feature 2 is working")

a1 = A()
b1 = B()

a1.feature1()
a1.feature2()

b1.feature1()
b1.feature2()


# lecture 61

class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("Feature 1 is working")

# B is Sub class of A so B inherites everything of A
class B(A):
    def __init__(self):
        print("In B init")
        super().__init__()
    def feature2(self):
        print("Feature 2 is working")

a1 = A()
b1 = B()


class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("Feature 1-A is working")

class B:
    def __init__(self):
        print("In B init")
    def feature1(self):
        print("Feature 1-B is working")

class C(B, A): #C(A, B) always inherites first class if method name is same
    def __init__(self):
        super().__init__()
        print("In C init")


c1 = C()
c1.feature1()


# Lecture 63 -> Duck typing

class Pulsar:
    def execute(self):
        print("A")

class MyEditor:
    def execute(self):
        print("A")
        print("B")

class Laptop:
    def code(self, ide):
        ide.execute()

# ide = Pulsar
ide = MyEditor()
lap = Laptop()

lap.code(ide)

# Lecture 64 -> Operator Overloading

class Student:

    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a + other.a
    def __gt__(self, other):
        return self.a > other.a
    def __getvalue__(self):
        return self.a

s1 = Student(25)
s2 = Student(30)

sum = s1.__add__(s2)
print(sum)

if s1.__gt__(s2):
    print("s1 bigger")
else:
    print("s2 bigger")

print(s1.__getvalue__())


# Lecture 65 -> method Overloading and overriding

from abc import ABC, abstractmethod

class Computer():
    def process(self):
        pass

# class Laptop(Computer):
#     def process(self):
#         print("It's running")

com = Computer()
com.process()

## generator lecture -68

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        pass

values = TopTen()


def Expert():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1
values = Expert()

print([a for a in values])
