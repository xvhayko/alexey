a = int(input("Введите число"))
if a > 9999 or a < 100000 :
    print()
a = a%100
d = a// 10
a = a%10
print(a)
print(d)
