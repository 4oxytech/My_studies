import os

list_paths = []


for adress, papka, file in os.walk('C:\\'):
    for i in file:
        full_path = os.path.join(adress, i)
        list_paths.append(full_path)



r = open('text.txt', 'w')
for x in list_paths:
    r.write(x + '\n')

r.close
