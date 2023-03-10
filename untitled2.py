a = float(input("сторона квадрата"))
b = float(input("радиус"))
c=a**2
h=b**2*3.14
if c < h:
    print('круг больше')
elif h == c:
    print('равны')
else:
    print('квадрат больше')