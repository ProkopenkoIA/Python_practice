# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random 
def add(massiv, dif):
    var = range(dif['a'], dif['b']+1)
    var = tuple(var)
    answer = []    
    for i in range(0, len(massiv)):
        if var.count(massiv[i]):
            answer.append(i)
    return answer        

         

    return answer

def read_value(answer):
    
    flag = 0
    a = int(input('Введите нижнее значение диапазона A: '))
    answer['a'] = a
    while flag==0:
        b = int(input('Введите верхнее значение диапазона B: '))
        if b<a:
            print('Значение B не может быть меньше А')
        else:
            answer['b'] = b    
            flag=1

def set_value(massiv, n):    
    for i in range(0, n):
        massiv.append(random.randint(-100, 101))
        
    return(massiv)

length = 9
massiv = [] 
dif = {'a':0, 'b':0}

set_value(massiv, length)
read_value(dif)
print('Исходный массив {}'.format(massiv))
print('Индексы цифр, попадающих в диапозон: {}'.format(add(massiv, dif)))

