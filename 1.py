a = int(input("Введите 3х значное число"))
if a > 999 or a < 100:
    print("плохое число")
else: 
    a1 = a // 100
    a2 = a // 10 % 10
    a3 = a % 10
print(a - ((a3 * 100) + (a2 * 10) + a1))