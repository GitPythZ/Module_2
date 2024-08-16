# import random
# numbers = list(range(3, 21))
# print(f"Дан список целых чисел: {numbers}")
# rand_inx = random.randint(0, len(numbers) + 1)
# rand_num = numbers[rand_inx]
# print(f"Сейчас появится случайное число из списка {numbers}: {rand_num}")
#     #"""Далее идет цикл 'while' для поиска всех делителей числа, которое выдает 'первая' вставка."""
# n = rand_num
# i = 1
# lst_divisors = []
# while i <= n**0.5:
#     if n % i == 0:
#         lst_divisors.append(i)
#         if i != n//i:
#             lst_divisors.append(n//i)
#     i += 1
# lst_divisors.sort()
# print(lst_divisors)
# password_lst = []
# for div_ in lst_divisors:
#     x = div_
#     if x <= 2:
#         continue
#     lst = list(range(1, x))
#     password_lst = []
#     for i in lst:
#         for j in lst:
#             if i + j == x and i == j:
#                 break
#             if i + j == x and i not in password_lst and j not in password_lst:
#                 password_lst.append(i)
#                 password_lst.append(j)
#     print(password_lst)

# import math
#import random
# Один из вариантов - использовать линейный конгруэнтный генератор псевдослучайных чисел.
# Например, чтобы получить все числа от 0 до 99, используйте начальное приближение - любое x,
# например,x=17 а затем вызывайте сто раз процедуру x = (21*x+1) mod 100. Ясно, что для получения всех чисел от 1 до 100
# нужно прибавить единичку к полученной последовательности, то есть на каждом шаге делать y[i]=x+1,
# тобы получить массив y[] с желаемым для вас свойством. Более точно подбор коэффициентов линейного
# генератора рассмотрен по ссылке.
# Второй способ - создать массив чисел от 1 до 100 и случайно его перемешать.

# Далее нужно подобрать формулу, которая будет отыскивать делители числа.
# def div_num(n):
#     return sorted({x for i in range(1, int(n**0.5) + 1) if n % i == 0 for x in (i, n//i)})
# print(div_num(20))
# n = int(input("Введите целое число: "))
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end=" ")
#     i += 1
# n = int(input("Введите целое число: "))
# i = 1
# while i <= n//2:
#     if n % i == 0:
#         print(i, end=" ")
#     i += 1
# n = int(input("Введите целое число: "))
# i = 1
# lst = []
# while i <= n**0.5:
#     if n % i == 0:
#         if i == n//i:
#             lst.append(i) # лист аппенд повторяется в условиях - его можно вынести зща скобку - см. ниже
#         else:
#             lst.append(i)
#             lst.append(n//i)
#     i += 1
# sorted(lst)
#print(lst)


# def sum_to_n(n, size, limit=None):
#     """Функция возвращающая список из 'size' положительных целых чисел,
#     которые в сумме дают число 'n'."""
#     if size == 1:
#         yield [n]
#         return
#     if limit is None:
#         limit = n
#     start = (n + size - 1) // size
#     stop = min(limit, n - size + 1) + 1
#     for i in range(start, stop):
#         for tail in sum_to_n(n - i, size - 1, i):
#             yield [i] + tail
# for partition in sum_to_n(6, 2):
#     print(partition)


# m = 5
#
# for i in range(1, 10, m):
#     for j in range(1, 10):
#         for k in range(m):
#             l = i + k
#             print(f"{l}\tX\t{j}\t=\t{l * j}", end="\t\t\t\t")
#         print()
#
#
#     print()

# import random
# s = random.randint(1, 10)
# print("char: ", s)
# spisok, res = [-5, -4, -2, -1, 0, 1, 2, 3, 4, 5], []
# for i in range(len(spisok)):
#     for x in range(len(spisok)):
#         if i == x:
#             continue
#         if spisok[i] + spisok[x] == s:
#             res += [[spisok[i] + spisok[x]]]
# for k in res[:len(res) // 2]:
#         print(k[0], k[1])
# print("count_combinations:", len(res) // 2)

# Получение случайного числа и его делителей
import random
numbers = list(range(3, 21))
print(f"Дан список целых чисел: {numbers}")
rand_inx = random.randint(0, len(numbers))
rand_num = numbers[rand_inx]
print(f"Сейчас появится случайное число из списка {numbers}: {rand_num}")
    #"""Далее идет цикл 'while' для поиска всех делителей числа, которое выдает 'первая' вставка."""
n = rand_num
i = 1
lst_divisors = []
while i <= n**0.5:
    if n % i == 0:
        lst_divisors.append(i)
        if i != n//i:
            lst_divisors.append(n//i)
    i += 1
lst_divisors.sort()
print(lst_divisors)
x = n
lst_ = list(range(1, x))
unique_lst = []
for i in lst_:
    for j in lst_:
        if i + j == x and i == j:
           break
        if i + j == x and i not in unique_lst and j not in unique_lst:
            unique_lst.append(i)
            unique_lst.append(j)
print(unique_lst)




