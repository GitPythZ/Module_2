numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = []
not_primes = []
mini_numbers = []
is_prime = True
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
                is_prime = True
                break
            else:
                is_prime = False
        if not is_prime:
            primes.append(i)
            mini_numbers.append(i)
print(primes)
print(not_primes)


