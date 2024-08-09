first = int(input("Введите целое число: "))
second = int(input("Введите целое число: "))
third = int(input("Введите целое число: "))
if first == second == third:
    print("3")
elif first==second!=third or first==third!=second or second==third!=first :
    print("2")
elif first!=second!=third: #перепроверка.
    print("0")
else:
    print("0")