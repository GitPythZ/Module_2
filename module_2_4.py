numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
mini_numbers = []
is_prime = False
for i in numbers:
    if i == 1:
        continue
    if len(primes) == 0:
        primes.append(i)
        mini_numbers.append(i)
    else:
        for num in mini_numbers:
            if i % num == 0:
                not_primes.append(i)
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            primes.append(i)
        mini_numbers.append(i)
print(primes)
print(not_primes)





# #Примечания: учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
# Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться
# ни на что в диапазоне от 2 до этого числа(не включительно).
# Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break,
# когда найдёте делитель. (Не обязательно)
# Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime,
# в кругах разработчиков называются перменными-флагами(flag).





