import random
numbers = list(range(3, 21))
print(f"Дан список целых чисел: {numbers}")
rand_inx = random.randint(0, len(numbers) + 1)
rand_num = numbers[rand_inx]
print(f"Сейчас появится случайное число из списка {numbers}: {rand_num}")


def get_dividers(x):
    dividers = set()
    for i in range(1, int(x**.5) + 1):
        if not x % i:
            dividers.add(i)
            dividers.add(x // i)
    return dividers


def get_pairs(x):
    pairs = set()
    for i in get_dividers(x):
        for j in range(1, i):
            if j != i - j:
                pairs.add(''.join(map(str, sorted((j, i - j)))))
    return ''.join(sorted(pairs))


n = rand_num
print(f"Пароль для второй вставки:", get_pairs(n))

