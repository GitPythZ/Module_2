# numbers = [10, 40, 20, 30]
# for item in numbers:
#     print(item+2)
# numbers = [10, 40, 20, 30, -1, 3, 0]
# for i in numbers:
#     if i > 0:
#         print(i)
# else:
#     print('stop')
# numbers = [10, 40, 20, 30]
# numbers.sort()
# print(iter(numbers)) # <list_iterator object at 0x1021c9d50>
# for i in range(len(numbers)):
#     print(f"index {i}: value: {numbers[i]}")
# print(4%2)
import random

a = range(0,101)
print(a[0])
a = list(range(0,101,17))
print(a)
randon_lst = []
range(10)
for num in range(0, 11, 2):
    randon_lst.append(num)
print(randon_lst)
numbers_ = list(range(0,101))
lst_chet = []
lst_nechet = []
for i in numbers_:
    if i == 0:
        continue
    if i % 2 == 0:
        lst_chet.append(i)
    else:
        lst_nechet.append(i)
print(f"Четные числа диапозона: {lst_chet}, \nНечетные числа диапозона {lst_nechet}")

check_lst = list(range(0,101))
# lst_fibonacci = []
# a,b = 0, 1
# for num in lst_fibonacci:
#     a,b = b, b + a
# n = int(input("Введите количество чисел: "))
# my_lst = list(int(input(f"Введите число {i}:")) for i in range(1, n+1))
# print(my_lst)
import random
random_lst = [random.randint(1,100) for i in range(20)]
print(random_lst)
print(len(random_lst))
square = [x**2 for x in range(1,1001) if x % 3 == 0]
print(square)
print(len(square))
# Задача 1. Создание списка из чисел, возведенных в степень 2, начиная с 0 и заканчивая 9.
lst1 = [x**2 for x in range(0,10)]
print(lst1)
# Задача 2. Дана строка. Создать список из букв в строке.
_str = "Дай мне строку в списке"
list(_str)
print(_str)
#
_str = "Дай мне строку в списке"
lst_ = list(_str)
print(lst_)
# Задача 3. Создание списка из всех четных чисел от 1 до 100.
chetnyi_lst = [x for x in range(1,101) if x % 2 == 0]
print(chetnyi_lst)
# Задача 4. Создание списка из квадратов чисел от 1 до 10, которые являются четными.
squares2 = [x**2 for x in range(1,11) if x % 2 == 0]
print(squares2)
# Задача 5. Создание списка из чисел, которые делятся на 3 или на 5.
squares3_5 = [x for x in range(1,100) if x % 3 ==0 or x % 5 == 0]
print(squares3_5)
squares3_5 = [x for x in range(1,100) if x % 3 ==0 and x % 5 == 0]
print(squares3_5)
# Задача 6. Создание списка из целых чисел, которые являются степенями двойки.
# lst_square_2 = [x**x for x in range(1, 100) if x == 2**x]
# print(lst_square_2)
# Задача 7. Создание списка из квадратных корней чисел от 1 до 10.
coren_ = [x**(0.5) for x in range(1,10)]
print(coren_)
    print(fib)
# Задача от меня: Создай список из чисел фибонначи в диапозоне от 0 до 1000
fib_ = []
for i in range[0, 10]:
    a, b = 0, 1
    a, b = b, a +b
    if
        fib_.append(i)
else:
print(fib_)
