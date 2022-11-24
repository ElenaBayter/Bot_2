# 1.Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

print("Write a number from 1 to 7: ")
num = int(input())

if num < 6:
    print("Weekday")
else:
    print("Weekend")
