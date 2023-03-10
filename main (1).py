a = float(input("Первая скорость км/ч"))
b = float(input("Вторая скорость м/с"))
c = a * 3.6
if c < b:
    print('первая меньше')
elif c == b:
    print('равны')
else:
    print('первая больше')