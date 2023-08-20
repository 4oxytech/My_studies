age = float(input('Сколько Вам лет?\n'))
weight = float(input('Ваш вес?\n'))
height = float(input('Ваш рост?\n'))
bmi = weight / height ** 2

if age < 10 or weight > 500 or height > 300:
    print('Ошибочные входные данные')
else:
    bmi = weight / height ** 2
    bmi = round(bmi)


    if bmi < 18.5:
        description = 'Недостаточной массой тела'
    if bmi < 25.0:
        description = 'Нормальной массой тела'
    if bmi < 30:
        description = 'избыточной массой тела'
    else:
        description = 'ожирением'

print(f'''bmi = {bmi}
Вы относитесь к группе людей с {description}''')

