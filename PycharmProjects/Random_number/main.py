import random
random_number = random.randint(1, 5)
user_number = int(input('Назовите число (от 1 до 10), кто угадал, тот загадывает желание, тому кто не смог отгадать, загадывать по-очереди: '))
if user_number == random_number:
 print('Кто-то из вас угадал число')
else:
    print("Ты не угадал :(")
    print(f'Было загадано число: {random_number}')

input()