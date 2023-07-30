# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите длину списка n: '))

m = int(input('Введите длину списка m: '))

list_n = list()
list_m = list()

set_m = set()
set_n = set()
answer = set()

i = 1

while i<=n:
    intem = int(input('Введите значение элемента списка n: '))
    list_n.append(intem)
    i+=1

i = 1

while i<=m:

    intem = int(input('Введите значение элемента списка m: '))
    list_m.append(intem)
    i+=1


#чтобы оставть уникальные значения, поместим списко в множество
for item in list_n:
    set_n.add(item)

for item in list_m:
    set_m.add(item)    


answer = set_n.intersection(set_m)

print(answer)