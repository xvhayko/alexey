a = int(input("Введите число"))
if a>999 or a<10000:
    print()
b = a//1000
a = a % 1000
c = a//100
a = a % 100
d = a //10
a = a % 10
z = b + d + c + a
p = a * b * d * c
print(z)
print(p)