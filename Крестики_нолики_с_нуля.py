# # def check_winners():
# #     for i in fields
# #     pass
#
#
# check_winners()


fields = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print(fields[0][0:3])
area = [["+", "-", "*"], ["=", "*", "/"], ["%", "//", "@"]]
print(area)
for i in area:
    print(i)
n = 0
for i in area[n][:]:
    for j in area[n + 1][:]:
        for k in area[n + 1][:]:
            print(i, j, k)
    n += 1
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("XOXOXOXOX*****Добро пожаловать в Крестики_Нолики*****OXOXOXOXO")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


def draw_fields():
    for i in fields:
        print(*i)


draw_fields()
for turn in range(1,10):
    print(f"Ход {turn}")
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят Нолики")
    else:
        turn_char = "X"
        print("Ходят Крестики")
    row = int(input("Введите номер строки (1, 2, 3): ")) - 1
    columns = int(input("Введите номер столбца (1, 2, 3): ")) - 1
    if fields[row][columns] == "*":
        fields[row][columns] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        draw_fields()
        continue
    draw_fields()