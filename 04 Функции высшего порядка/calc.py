
# Задача 36: Напишите функцию вывода таблицы умножения print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**


def print_operation_table(operation, num_rows=6, num_columns=6):
     for x in range(1,num_rows+1):
          a = operation(x,num_columns)        
          a = ' '.join(str(s) for s in a)  
          print(a)

def lst(a,rows):
    return [a*x for x in range(1,rows+1)]

print_operation_table(lst)