fields = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("XOXOXOXOX*****Добро пожаловать в Крестики_Нолики*****OXOXOXOXO")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


def draw_fields():
    for i in fields:
        print(*i)

def check_winners():
    if fields[0][0:3] == ["X", "X", "X"]:
        return "X"
    if fields[1][0:3] == ["X", "X", "X"]:
        return "X"
    if fields[2][0:3] == ["X", "X", "X"]:
        return "X"
    if fields[0][0] == "X" and fields[1][0] == "X" and fields[2][0] == "X":
        return "X"
    if fields[0][1] == "X" and fields[1][1] == "X" and fields[2][1] == "X":
        return "X"
    if fields[0][2] == "X" and fields[1][2] == "X" and fields[2][2] == "X":
        return "X"
    if fields[0][0] == "X" and fields[1][1] == "X" and fields[2][2] == "X":
        return "X"
    if fields[0][2] == "X" and fields[1][1] == "X" and fields[2][0] == "X":
        return "X"
    if fields[0][0:3] == ["O", "O", "O"]:
        return "O"
    if fields[1][0:3] == ["O", "O", "O"]:
        return "O"
    if fields[2][0:3] == ["O", "O", "O"]:
        return "O"
    if fields[0][0] == "O" and fields[1][0] == "O" and fields[2][0] == "O":
        return "O"
    if fields[0][1] == "O" and fields[1][1] == "O" and fields[2][1] == "O":
        return "O"
    if fields[0][2] == "O" and fields[1][2] == "O" and fields[2][2] == "O":
        return "O"
    if fields[0][0] == "O" and fields[1][1] == "O" and fields[2][2] == "O":
        return "O"
    if fields[0][2] == "O" and fields[1][1] == "O" and fields[2][0] == "O":
        return "O"
    return "*"


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
    if check_winners() == "X":
        print("Победа Крестиков")
        break
    if check_winners() == "X":
        print("Победа Ноликов")
        break
    if check_winners() == "*" or turn == 9:
        print("Ничья")