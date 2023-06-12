a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
if a >= b:
    print("Ошибка: A должно быть меньше B")
else:
    i = a + 1
    while i < b:
        print(i)
        i += 1