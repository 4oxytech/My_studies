#Мы работаем в фирме, перед нами стоит задача: создать функцию
#алгоритм которой, будут использовать другие разработчики
#они будут передовать туда списки с данными, сколько бы у них их не было.
#А функция будет выдавать результат, тоже список, только все значения будут уникальными
#То есть повторяющиеся значения будут отсеиваться, из всех списков, которые были переданы
#будет сформирован один с уникальными значениями.


# def exclusive_item(*args):
#     #args будет возвращать новый список
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
#     return new_list
#
#
#
#
#
# z = [9, 8, 7]
# x = [8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]
#
# t = exclusive_item(z, x, c)

def exclusive_list(*args, keys = False):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if keys == True:
        new_list.sort()
        return new_list


x = [1, 2, 3, 5, 4, 5, 7, 8]
z = [3, 9, 5, 6, 10]
t = exclusive_list(x, z, keys=True)
print(t)

