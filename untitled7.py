a = int(input())
b = int(input())
if a < b:
    while True:
        a += 1
        if a == b:
            break
        else:
            print(a)