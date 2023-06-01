def bank(a,time):
    for each_year in range(time):
        a = (a * 1.1)
    return a
a=float(input("количество вкладываемых денег"))
time=int(input("На сколько лет?"))
print(bank (a, time))