#Изучение циклов: Цикл while, который печатает числa в порядке возрастания
def print_number(last_number):
    i = 0
    while i <= last_number:
        i += 1
        print(i)
    print('Finished')

print_number(5)


#Изучение циклов: Цикл while, который печатает числa в обратном порядке
def print_number(number):
    i = number
    while i > 0:
        i -= 1
        print(i)

print_number(10)

#Реализуйте функцию, которая будет считать произведение чисел, заданного дипазона
def multiply_numbers_from_range(start, finish):
    result = 1
    i = start
    while i <= finish:
        result *= i
        i += 1
        print(result)
multiply_numbers_from_range(2, 5)

#Реализуйте функцию, которая будет объединять все числа из диапазона в строку
def join_numbers_from_range(start, finish):
    result = ''
    i = start
    while i <= finish:
        result = result + str(i)
        i += 1
    return result

x = join_numbers_from_range(1, 10)
print(x)



#которая печатает переданное слово посимвольно,но делает это в обратном порядке.
def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i = i - 1
print(print_reversed_word_by_symbol('lera'))

#Представьте функцию, которая считает, сколько раз входит буква в предложение
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].lower() == char.lower():
            count += 1
        index += 1
    return count
print(count_chars('lera', 'a'))