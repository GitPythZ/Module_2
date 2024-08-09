# name = input("Введите ваше имя: ")
# if name == "Анатолий":
#     print("Здравствуйте, Администратор")
# if name == "Динара":
#     print("Привет, жена!")
# else:
#     print("Привет", name)
number = int(input("Введите число: ")) # Fizz (число кратно 3), Buzz(число кратно 5), FizzBuzz (число кратно и 3, и 5)
if number % 3 == 0:
    print("Fizz")
if number % 5 == 0:
    print("Buzz")
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
# elif - он говорит, что этол условие будет выполняться только, если предыдущее не выполнилось
# На будущее, лучше самые тяжело выполниме условия располагать сверху, помечать егшо if, а последующие уже elif
# Тогда ты будешь закономерно получать нужнеые значения
number = int(input("Введите число: ")) # Fizz (число кратно 3), Buzz(число кратно 5), FizzBuzz (число кратно и 3, и 5)
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Число не кратно 3 и/или 5")
