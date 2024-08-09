# Стиль кода, цикл while
#while 1 > 0:  #while - повторяется до тех пор, пока True, @if@ повторяется однократно
    #number = int(input("ведите число: "))
    #if number % 2 == 0:
      #  print("Число чётное")
        #continue  #запускает цикл заново, пропуская все услвиия, идущие ниже1
    #else:
  #      print("Число нечётное")
   # print("AAA")  #break
#print("Я за циклом")

#Бесконечный цикл пока не внесу break
lst = [322, 5236, -1, 23, 64, 82]
i = len(lst) - 1
while i >= 0:
    if lst[i] > 0:
        print(lst[i])
    i = i - 1
