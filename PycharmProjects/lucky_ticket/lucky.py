q = input('go')
#Счастливый номер билета
def is_happy_number(s):
    res1 = 0
    res2 = 0
    for i in range(len(s) // 2):
        res1 += int(s[i])
        res2 += int(s[len(s) // 2 + i])
    if res1 == res2:
        print(f'{s} счастливый номер')
    else:
        print(f'{s} не счастливый номер')
is_happy_number(q)