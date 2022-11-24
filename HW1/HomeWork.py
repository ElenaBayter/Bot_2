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



# # 2.Напишите программу для проверки истинности утверждения
# # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Write a {xyz[i]}: "))
#     return a
#
# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result
#
# statement = inputNumbers(3)
#
# if checkPredicate(statement) == True:
#     print(f"Statement is true")
# else:
#     print(f"Statement is false")



# # 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# # в которой находится эта точка (или на какой оси она находится).
#
# print("Write a number x: ")
# x = int(input())
#
# print("Write a number y: ")
# y = int(input())
#
# if x > 0 and y > 0:
#     print("Our point located in I quater")
#
# if x < 0 and y > 0:
#     print("Our point located in II quater")
#
# if x < 0 and y < 0:
#     print("Our point located in III quater")
#
# if x > 0 and y < 0:
#     print("Our point located in IV quater")


# # 4.Напишите программу, которая по заданному номеру четверти,
# # показывает диапазон возможных координат точек в этой четверти (x и y).
#
# print("Write a number of quater: ")
# q = int(input())
#
# if q == 1:
#     print("Point coordinates is (x>0, y>0)")
#
# if q == 2:
#     print("Point coordinates is (x<0, y>0)")
#
# if q == 3:
#     print("Point coordinates is (x<0, y<0)")
#
# if q == 4:
#     print("Point coordinates is (x>0, y<0)")



# # 5.Напишите программу, которая принимает на вход координаты двух точек
# # и находит расстояние между ними в 2D пространстве
#
# print("Write x coordinate for first point: ")
# x1 = int(input())
# print("Write y coordinate for first point: ")
# y1 = int(input())
# print("Write z coordinate for first point: ")
# z1 = int(input())
# print("Write x coordinate for second point: ")
# x2 = int(input())
# print("Write y coordinate for second point: ")
# y2 = int(input())
# print("Write z coordinate for second point: ")
# z2 = int(input())
#
# d = (((x2-x1) ** 2) + ((y2-y1) ** 2) + ((z2-z1) ** 2)) ** 0.5
# print(round(d, 2))