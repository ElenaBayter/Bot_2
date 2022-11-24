# # 1.Напишите программу, которая принимает на вход цифру,
# # обозначающую день недели, и проверяет, является ли этот день выходным.
#
# print("Write a number from 1 to 7: ")
# num = int(input())
#
# if num < 6:
#     print("Weekday")
# else:
#     print("Weekend")


# 2.Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Write a {xyz[i]}: "))
    return a

def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Statement is true")
else:
    print(f"Statement is false")
