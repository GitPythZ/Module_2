import random


def password():
    list_password = []
    lock = 0
    range_lock = range(3, 21)
    number_lock = random.choice(range_lock)
    lock += number_lock
    range_password = range(1, 21)
    for i in range_password:
        range_password_2 = range(i + 1, 21)
        for j in range_password_2:
            if i != lock and j != lock and lock % (i + j) == 0:
                list_password.append(i)
                list_password.append(j)

    print(f'{lock} - число из первой вставки')
    print(*list_password, '- нужный пароль')


password()

