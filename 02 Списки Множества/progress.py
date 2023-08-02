# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def read_value(value):
    
    a = int(input('Введите значение первого элемента a1: '))
    n = int(input('Введите длину прогрессии n: '))
    d = int(input('Введите размер шага d: '))
    value['a']=a
    value['d']=d
    value['n']=n
    

def progress(value):
    answer = []
    step = 2
    answer.append(value['a'])
    print('Шаг {} значение {}'.format(1,answer))
    while step<=value['n']:
        answer.append(value['a']+(step-1)*value['d'])
        print('Шаг {} значение: {}'.format(step,answer))
        step+=1
    return(answer)

value = {'a':0, 'n':0, 'd':0}

read_value(value)
progress(value)

