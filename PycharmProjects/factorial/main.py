#Факториал числа
while True:
    x = int(input("Введите число"))
    y = 1
    count = 0
    while count < x:
        count += 1
        y *= count
    else:
        print(y)