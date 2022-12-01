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