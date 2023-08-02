# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение
def stepen(value,count):    
    if count == 0:
        return 1    
    return value*stepen(value,count-1)
      
a = 2
b = 2

print(stepen(a,b))
