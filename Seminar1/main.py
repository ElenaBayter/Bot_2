# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
import random

# print("Write a number a")
# a = int(input())
#
# print("Write a number b")
# b = int(input())
#
# if a**2==b or b**2==a:
#     print(f"Yes one of numbers a is square of other number")
#
# else:
#     print("No")



# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# num = []
# for i in range(5):
#     x = int(input("Write a number: "))
#     num.append(x)
# max_t = num[0]
# for i in num:
#     if i > max_t:
#         max_t = i
# print(max_t)



# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# num1 = float(input("Write a number "))
# num2 = int(num1)
# if num1 == num2:
#     print("integer")
# else:
#     num2 = int(num1*10) % 10
# if num2 != 0:
#     print(num2)
# else:
#     print('zero')
# if num2 != 0:
#     print(num2)
# else:
#     print('zero')


size = int(input('Write array size: '))

my_list = []
for i in range(size):
    my_list.append(random.randint(1, 100))

print(my_list)


my_list = [random.randint(0, 100) for _ in range(10)]
print(my_list)