# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# 1, -3, 9, -27, 81

from decimal import Decimal

#
# my_list = []
# n = int(input("Write a number n: "))
#
# for i in range (n):
#     my_list.append((-3)**i)
#
# print(*my_list, sep = ', ')




# Для натурального n создать список,
# состоящий из элементов последовательности 3*n + 1.
#
# Для
# n = 6: ['1: 4', '2: 7', '3: 10', '4: 13', '5: 16', '6: 19']


# n = int(input("Write a number: "))
# my_list = []
#
# for i in range(1, n+1):
#     my_list.append(str(i) + ': ' + str(3*i+1))
# print(my_list)


# COORDINATES
#
# coords = input('Write a coordinates: ')
# coords = coords.split(' ')
#
# if len(coords)/2 == 2:
#     print('2D')
# elif len(coords)/2 == 3:
#     print('3D')
# else:
#     print('You write incorrect coordinates')



# number = float(input('Write a size of list: '))
#
# number0 = (number*100)/10
#
# numberD = (Decimal(str(number))*100)/10
#
# print(number0)
# print(numberD)




# numbers = input('Write a number: ')
# count = int(input('Write a accuracy'))
#
# print(numbers)
# numbers = numbers.split('.')
#
# print(float(numbers[0] + '.' + numbers[1][0:count]))



# numbers = int(input('Write a size of list: '))
# my_list = [i for i in range(numbers)]
#
# print((my_list))
# print(my_list[:-3])



# numbers = int(input('Write a number: '))
#
# my_list = []
#
# for i in range(-numbers, numbers+1):
#     my_list.append(i)
#
# print(*my_list, sep=' next number ', end=' finish')




# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# from decimal import Decimal as Dcm
# number = Dcm(input('Write a number: '))
# count = 0
# while number%1 != 0:
#     number *= 10
#
# new_number = int(number)
# while ((new_number*10)//10) != 0:
#     count += new_number % 10
#     new_number //= 10
# print(count)


# Second option, but really it's not work, I'll appreciate for advices!!!!

# my_list = [str(number)]
# print(*my_list)
# for i in range(0, len(my_list)+1):
#     count = count + i
# print(count)




# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
#
# n = int(input("Write a number: "))
# my_list = []
#
# for i in range(1, n+1):
#     my_list.append(float(round(((1 + 1 / i) ** i), 2)))
# print(*my_list)
# sum1 = 0
# count = 0
# while count < len(my_list):
#     sum1 += my_list[count]
#     count += 1
# print(sum1)



# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# import random, random
#
# num = int(input("Write a size of list: "))
# # my_list = [i for i in range(num)]
#
# my_list = []
# for i in range(num):
#     my_list.append(i)
# print(*my_list)
# new_list = my_list[:]
# for i in range(len(new_list)):
#     index = random.randint(0, len(my_list)-1)
#     if my_list[index+1] != my_list[index]:
#         new_list.append(my_list[index])
# print(new_list)



# for i in range(len(new_list)):
#     index = random.randint(0, len(my_list))
#     temp = new_list[i]
#     new_list[i] = my_list[index]
#     my_list[index] = temp
# print(new_list)



# SEMINAR_3
#
# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# my_list = ['guyfguy45568687', 'hgytd09556', 'hvhhj0896', 'jhfghgc346']
# simbol = input('Write a simbol: ')
# for item in my_list:
#     count = 0
#     for i in range(len(item)):
#         if simbol == item[i]:
#             count +=1
#             print(f'Simbol {simbol} is in string {item} on {i} position')
#     print(f'Simboln {simbol} is in string {item} {count} times')

    # else:
    #     print(f'Simbol {simbol} is NOT in {item}')



# Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: False
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: False
# - список: [], ищем: "123", ответ: False
#
# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# search_string = input("Write a symbol: ")
# count = 0
# print(my_list)
# for i in range(len(my_list)):
#     if my_list[i] == search_string:
#         count+=1
#     if count == 2:
#         print(f'The searching string {search_string} is on position {i}')
#         break
# else:
#     if count == 1:
#         print(f'The searching string {search_string} is not repeat')
#     else:
#         print(f'The searching string {search_string} is not found')





#
#  Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
#
# text = 'First digit - 1, second digit - 2, sum 3'
# sub_text = input("Write sub string")
# count = 0
# for i in range(len(text)):
#     if text[i:i+len(sub_text)] == sub_text:
#         count += 1
# print(f'Sub string {sub_text} met in our text {count} times')


#### print(text.count(sub_text))





# text = "First number"
# print(text[0:8])     #First nu






# import random, random
#
# num = int(input("Write a size of list: "))
# # my_list = [i for i in range(num)]
#
# my_list = []
# for i in range(num):
#     my_list.append(i)
# print(*my_list)
# new_list=[]
# for i in my_list:
#     i=random.randrange(len(my_list))
#     new_list.append(i)
# print(new_list)





# import random, random
#
# num = int(input("Write a size of list: "))
# # my_list = [i for i in range(num)]
#
# my_list = []
# for i in range(num):
#     my_list.append(i)
# print(*my_list)
# new_list = my_list[:]
# for i in range(len(new_list)):
#     index = random.randint(0, len(my_list)-1)
#     if my_list[index+1] != my_list[index]:
#         new_list.append(my_list[index])
# print(new_list)





# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# print(my_list)
# sum = 0
# for i in range(len(my_list)):
#     if i%2 != 0:
#         sum += my_list[i]
# print(sum)




# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


# size = int(input('Write a size of list'))
# my_list = []
# for i in range(size):
#     my_list.append(i)
# print(*my_list)
# count = 0
# steps = 0
# new_list = []
# for i in range(len(my_list)):
#     count = int(my_list[0+i] * my_list[-1-i])
#     steps += 1
#     new_list.append(count)
#     if steps >= len(my_list)/2:
#         break
# print(new_list)



# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random, random

# size = int(input("Write a size of list: "))
#
# my_list = []
# for i in range(size):
#     i = random.uniform(0, 10000)
#     my_list.append(round(i, 2))
# print(*my_list)
# new_list = []
# desim = 0
# for i in range(len(my_list)):
#     desim = my_list[i]-int(my_list[i])
#     new_list.append(round(desim, 2))
# print(*new_list)
# max_desim_number = max(new_list)
# print(max_desim_number)
# min_desim_number = min(new_list)
# print(min_desim_number)
# result = max_desim_number - min_desim_number
# print(f'Difference between maximal and minimal fractional parts of elements is {round(result, 2)}')












# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number = int(input('Write a number: '))
# double_num = []
# div = 0
# while number > 0:
#     div = number % 2
#     double_num.append(div)
#     number //= 2
# print(*double_num[::-1])



  # SECOND OPTION

# number = int(input('Write a number: '))
# double_num = ''
# while number > 0:
#     double_num = str(number % 2) + double_num
#     number //= 2
# print(double_num)




# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# n = int(input("Write a size of list: "))
# fib_array = []
# for i in range(n):
#     if i == 0:
#         fib_array[i] = 0
#         fib_array.append(fib_array[i])
#     if i == 1:
#         fib_array[i] = 1
#         fib_array.append(fib_array[i])
#     else:
#         fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
#         fib_array.append(fib_array[i])
# for i in range(-n, 0):
#     if i == 0:
#         fib_array[i] = 0
#         fib_array.insert(fib_array[i])
#     if i == 1:
#         fib_array[i] = 1
#         fib_array.insert(fib_array[i])
#     else:
#         fib_array[i] = fib_array[i - 1] - fib_array[i - 2]
#         fib_array.insert(fib_array[i])
# print(fib_array)



# OTHER OPTION
# f1 = 0
# f2 = 1
# print(f1, f2, end=' ')
# for i in range(-n, 0):
#     f1, f2 = f2, f1 - f2
#     print(f2, end=' ')
# fib1 = fib2 = 1
# print(fib1, fib2, end=' ')
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

# BOTH OF OPTIONS DOESN'T WORK, BUT I WROTE HOW I UNDERSTAND. SORRY(((((
