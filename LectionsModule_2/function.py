def triangle(size, symb):
    for i in range(1, size + 1):
        print(symb*min(i, size - i + 1))
triangle(9, ".")

def mean_arith(*args):
    summa = 0
    total = 0
    for i in args:
        summa += i
        total += 1
    return summa/total
print(mean_arith(5, 5, 15, 25, 35))
def sort_lst(st):
    numb_ = [x for x in st if x.isdigit()]
    letters = [x for x in st if x.isalpha()]
    spec_char = [x for x in st if x.isalnum()]
    print(*numb_)
    print(*letters)
    print(*spec_char)
my_st = input("Введите любую последовательность знаков: ") #23edwd893rjf934#$%Ye34F^(*))_+W$#Ddq2ddscew3r
sort_lst(my_st)
def new_year_bonus(name, last_name, salary = 120000, bonus = 10):
    print(f"Новогодняя премия сотрудника {name} {last_name} составила: {salary * bonus / 100:.2f} руб,\n"
          f"Оклад сотрудника составил : {salary:.2f} руб.\n"
          f"Всего получено на руки: {salary + salary * bonus / 100:.2f} руб.\n")
new_year_bonus("Anton", "Ivanov", 120000, 10)
def func(n):
    for i in range(n):
         yield i
a = list(func(4))
print(a)