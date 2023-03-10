a = int(input("Обьем: "))
b = int(input("Масса: "))
a1 = int(input("Обьем2: "))
b1 = int(input("Масса2: "))
c = a * b
f = a1 * b1
if c < f:
    print('первая меньше')
elif c == f:
    print('равны')
else:
    print('первая больше')