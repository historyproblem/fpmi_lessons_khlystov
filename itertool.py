import itertools
# from itertools import repeat
#
# alphabet = "abc123"
# length = 3
# for j in range(1,5):
#     for combo in itertools.product("abc1323", repeat=j):
#         s = ''.join(combo)
#         if s[0] == '1':
#             print(s)

# for p in itertools.permutations("abc132", repeat=2):
#     if p[0] == 1:
#         print(p)
#     s = ''.join(p)
#     print(''.join(p))  # ab, ac, ba, bc, ca, cb

# for c in itertools.combinations("abc", 2):
#     print(''.join(c))  # ab, ac, bc
#
# for c in itertools.combinations_with_replacement("abc", 2):
#     print(''.join(c))  # aa, ab, ac, bb, bc, cc

# Пример 1
#
# s1 = "daaddaaada"
# s2 = "dd"
# s3 = ""
# arr = s1.split('d')
# print(s1.split('d'))
# print(s2.split('d'))
# print(s3.split('d'))
# print(*arr)
# string = ' po lps ;le \n'
# print(string.strip())
# print(string.lstrip())
# print(string.rstrip())
# ['', 'aa', '', 'aaa', 'a']
# ['', '', '']
# ['']

# ============================#
# Пример 2
    # s = 'apple.'
    # s = s[:]
    # # print(s[:len(s) - 1].count('.'))
#==============================#

# # Пример 3
# s = '1'
# a = '3'
# b = int(s) + int(a)
# c = s + a
# print(b,c)

#================================#

# replace
#
# sss = 'lskdfmm'
# print(sss.replace('kdf', 'aa')))

#===================================#
# arr = ['1', 1, 'tun', ['1', '2']]
# print(arr)
# print(*arr)
#====================================#

# my_dict = {}
# user = {"name": "Alice", "age": [30, 0], "city": {"first":"Paris", "second":"Moscow"}}
# user["name1"] = 533
# print(user.get("name", "Ключ не найден"))
# email = user.pop("email")

# for key, value in user.items():  # По парам ключ-значение
#     print(f"{key}: {value}")
#
# print(user["name1"])
#==================#

# pattern = re.compile(r'(?=([A-Z][a-z]*(?: [A-Z]?[a-z]+)*\.))')
#
'''
^
|
решение через регулярки

(№ 8058) (Пробный ЕГЭ, г. Томск) Текстовый файл 24-332.txt состоит не более чем из 106 символов и содержит только латинские буквы A, B, C, a, b, c, точки и пробелы. Определите максимальное количество символов в непрерывной последовательности, которая является корректно записанным предложением. Считаем, что в корректно записанном предложении выполнены все следующие условия:
– предложение начинается с заглавной буквы;
– предложение оканчивается точкой, которая в предложении единственная и перед которой нет пробела;
– слова в предложении состоят из произвольных комбинаций букв, возможно не имеют семантического смысла, но при этом только первая буква слова может быть заглавной;
– слова в предложении разделены пробелами, два пробела стоять рядом в предложении не могут.
В ответе укажите количество символов.
Ответ: 22.
'''


def is_upper_letter(c):
    return c.isupper()

# print('abc'.islower())
#
def is_valid_letter(c):
    return c!='.'


f = open("24-332.txt", "r")
text = f.readline().strip()

max_len = 0
n = len(text)

start = -1
word_start = -1
valid = 1

i = 0
while i < n:
    c = text[i]
    if start == -1:
        if is_upper_letter(c):
            start = i
            word_start = i
            valid = 1
        i += 1
        continue
    if c == ' ':
        if i > start and text[i - 1] == ' ':
            valid = 0
        word_start = i + 1

    elif c == '.':
        if i > start and text[i - 1] == ' ':
            valid = 0
        if valid:
            candidate_len = i - start + 1
            if candidate_len > max_len:
                max_len = candidate_len
        start = -1
        valid = 1
        i += 1
        continue

    else:
        if not is_valid_letter(c):
            valid = 0
        else:
            if i != word_start and c.isupper():
                valid = False

    if not valid:
        if is_upper_letter(c):
            start = i
            word_start = i
            valid = 1
        else:
            start = -1
            valid = 1
    i += 1

print(max_len)

# # Пример 1
# #
# # s1 = "daaddaaada"
# # s2 = "dd"
# # s3 = ""
# # arr = s1.split('d')
# # print(s1.split('d'))
# # print(s2.split('d'))
# # print(s3.split('d'))
# # print(*arr)
# # string = ' po lps ;le \n'
# # print(string.strip())
# # print(string.lstrip())
# # print(string.rstrip())
# # ['', 'aa', '', 'aaa', 'a']
# # ['', '', '']
# # ['']
#
# # ============================#
# # Пример 2
#     # s = 'apple.'
#     # s = s[:]
#     # # print(s[:len(s) - 1].count('.'))
# #==============================#
#
# # # Пример 3
# # s = '1'
# # a = '3'
# # b = int(s) + int(a)
# # c = s + a
# # print(b,c)
#
# #================================#
#
# # replace
# #
# # sss = 'lskdfmm'
# # print(sss.replace('kdf', 'aa')))
#
# #===================================#
# # arr = ['1', 1, 'tun', ['1', '2']]
# # print(arr)
# # print(*arr)
# #====================================#
#
# # my_dict = {}
# user = {"name": "Alice", "age": [30, 0], "city": {"first":"Paris", "second":"Moscow"}}
# user["name1"] = 533
# # print(user.get("name", "Ключ не найден"))
# # email = user.pop("email")
#
# for key, value in user.items():  # По парам ключ-значение
#     print(f"{key}: {value}")
#
# print(user["name1"])



# # Создаем список из 5 нулей
# n = 5
# list1 = [0] * n          # Способ 1
# list2 = [0 for _ in range(n)]  # Способ 2
#
# print("list1:", list1)    # [0, 0, 0, 0, 0]
# print("list2:", list2)    # [0, 0, 0, 0, 0]
#
# # Плохой способ:
# bad_matrix = [[0] * 3] * 3  # Создает 3 ссылки на ОДИН список
# bad_matrix[0][0] = 99       # Изменяем первый элемент первой строки
#
# print("bad_matrix:")
# for row in bad_matrix:
#     print(row)
# # Вывод:
# # [99, 0, 0]
# # [99, 0, 0]
# # [99, 0, 0]  <- Все строки изменились!
#
# # Хороший способ:
matrix = [([i for i in range(3)]) for j in range(3)]
print(matrix)
# # good_matrix[0][0] = 99  # Изменяем только первую строку
#
# print("\ngood_matrix:")
# for row in good_matrix:
#     print(row)
# # Вывод:
# # [99, 0, 0]
# # [0, 0, 0]
# # [0, 0, 0]
#
# # Плохо:
# bad_list = [[]] * 3     # Все элементы — одна и та же пустая список
# bad_list[0].append(1)   # Добавляем 1 в "первый" список
#
# print(bad_list)  # [[1], [1], [1]]  <- Все элементы изменились!
#
# # Хорошо:
# good_list = [[] for _ in range(3)]
# good_list[0].append(1)
# print(good_list)  # [[1], [], []]
#
# # Создаем список четных чисел от 0 до 10
# even_numbers = [x for x in range(11) if x % 2 == 0]
# print(even_numbers)  # [0, 2, 4, 6, 8, 10]
## #===========================================================================#
# #FILES
#
# file = open("example.txt", "r", encoding="utf-8")
# content = file.read()  # Читает весь файл в строку
# file.close()
# print(content)
#
# # with open("example.txt", "r", encoding="utf-8") as file:
# #     content = file.read()
# #     print(content)
#
#



