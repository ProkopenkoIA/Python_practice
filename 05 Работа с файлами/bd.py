import sqlite3 as sl
#from tabulate import tabulate


menu_list = ('1 - Показать справочник', '2 - Добавить абонента'
             ,'3 - Редактировать абонента', '4 - Удалить абонента '
             ,'5 - Поиск' 
             ,'6 - Добавить тип телефонного номера' 
             ,'7 - Добавить телефонный номер' 
             ,'8 - Импорт' 
             ,'0 - Выход')

add_list = ('1 - Добавить номер телефона', '2 - В основное меню',  '3 - Еще...'          
             ,'0 - Выход')

add_list2 = ('1 - Ещё...', '2 - В основное меню'       
             ,'0 - Выход')

phone_list = ('1 - Ещё...', '2 - В основное меню'       
             ,'0 - Выход')

select_table_list = ('1 - Users', '2 - Phones', '3 - PhoneType'  
                     , '4 - Основное меню'           
             ,'0 - Выход')


# Переопределение функции преобразования к нижнему регистру
def sqlite_lower(value_):
    return value_.lower()
  
# Переопределение функции преобразования к верхнему геристру
def sqlite_upper(value_):
     return value_.upper()

# Переопределение правила сравнения строк
def ignore_case_collation(value1_, value2_):
    if value1_.lower() == value2_.lower():
        return 0
    elif value1_.lower() < value2_.lower():
        return -1
    else:
        return 1 

def create_db(): 
    
    #Данные о контакте
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL DEFAULT '' COLLATE NOCASE,
    age INTEGER
    )''')
    #Телефонные номера
    cursor.execute('''CREATE TABLE IF NOT EXISTS Phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER NOT NULL,
    phone_type_id integer NOT NULL,
    phone_name TEXT NOT NULL,               
    value text NOT NULL               
    )''')
    #Типы телефонов
    cursor.execute('''CREATE TABLE IF NOT EXISTS PhoneType (
    id INTEGER PRIMARY KEY AUTOINCREMENT,                  
    value text NOT NULL               
    )''')
    connection.commit()  

#Меню

def menu():
    print('==>> Основное меню...')
    for item in menu_list:
        print(item)
    print('---------------------')      
    answer = int(input(f"Выберете пункт меню: "))
    if answer == 2:
        add_abonent()
    if answer == 1:
        select_table()  
    if answer == 4:
        delete_abonent(0)  
    if answer == 5:
        finde()            
    if answer == 6:
        add_phone_type()     
    if answer == 7:
        add_phone_menu()     
    if answer == 8:
        import_file()  
# Импорт

def import_file():    
    with open('import.txt',encoding='UTF-8') as f:  
        line = f.readline().split(';')
        try:
            cursor.execute('INSERT INTO users (username,age) Values (?, ?)', (line[0], int(line[1])))
            connection.commit
            cursor.execute('Select max(id) From users')
            id = cursor.fetchone()[0]
            cursor.execute('INSERT INTO Phones  (id_user , phone_type_id ,phone_name ,value) Values (?, ?,?, ?)', (int(id), int(line[2]), line[3], line[4],))
            connection.commit 
            print_finde_user(id)
        except:
            print('Не удалось произвести загрузку! Переход в основное мень')    
            menu()
        
#Поиск
def finde():
   print()
   print('==>> Поиск...')
   name = input(f"Ведиет имя абонента или нажмите 0, чтобы вернуться в меню: ")  
   if name !='0':
    sql = "Select id from  Users Where lower(username)  like ?" 
    cursor.execute(sql, ("%"+name.lower()+"%",)) 
    try:
        id = cursor.fetchone()[0]
        print_finde_user(id)
    except:
        a =   input(f"Поиск не дал результата, нажмите Enter") 
        finde()
    else:
        menu()    


# Выбор таблицы

def select_table():
    list = {1:"Users",2:"Phones",3:"PhoneType"}
    print('==>> Выбор таблицы для отображения...')
    for item in select_table_list:
        print(item)
    print('----------------')
    answer = int(input(f"Выберете пункт меню: "))
    if answer == 4:
        menu()
    print_table(list[int(answer)],1)     

#Добавление

def add_abonent():
    print('==>> Добавление абонента...')
    name = input(f"Введите имя абонента: ")
    age = input(f"Укажите возраст абонента: ")    
    cursor.execute('INSERT INTO users (username,age) Values (?, ?)', (name, int(age)))
    connection.commit
    cursor.execute('Select max(id) From users')
    id = cursor.fetchone()[0]
    for item in add_list:
        print(item)
    print('----------------')    
    answer = int(input(f"Выберете пункт меню: "))
    print()
    if answer == 1:
        add_phone(id)
    if answer == 2:
        menu() 
    if answer == 3:
        add_abonent()      

def add_phone_type():
    print('==>> Добавление типа телефонного номера...')
    name = input(f"Введите тип телефонного номера: ")  
    cursor.execute('INSERT INTO PhoneType (value) Values (?)', (name,))
    connection.commit    
    for item in add_list2:
        print(item)
    print('----------------')    
    answer = int(input(f"Выберете пункт меню: "))
    print()
    if answer == 1:
        add_phone_type()
    if answer == 2:
        menu() 


def add_phone_menu():
    print("==>> Добавление номера телефона для абонента")
    print_table('users',0)
    answer = int(input(f"Укажите индекс абонента "))
    add_phone(answer)

# Удаление
def delete_abonent(id):
    print("==>> Удаление абонента")
    if id ==0:
        print_table('users',0)
        id = int(input(f"Укажите индекс абонента "))
    # Отмена решения не помешала бы...
    sql = "delete FROM Users Where id = ?" 
    cursor.execute(sql, (id,)) 
    connection.commit()

    sql = "delete FROM Phones  Where id_user  = ?" 
    cursor.execute(sql, (id,)) 
    connection.commit()

    input(f"Абоненрт удален. Нажмите Enter чтобы вернуться в меню ")
    menu()


def add_phone(id):    
    cursor.execute('Select username From users Where id =?', (id,))
    name = cursor.fetchone()[0]
    print("==>> Добавление номера телефона для абонента: {}".format(name))
    sql = "SELECT * FROM PhoneType" 
    cursor.execute(sql)  
    results = cursor.fetchall()  
    strng = ''
    for row in results:
        strng = strng+str(row[0])+'-'+row[1]+'; '

    value  = input(f"Введите номер телефона: ")
    name = ''
    type = int(input("Укажите тип номера ({}): ".format(strng))    )
    cursor.execute('INSERT INTO Phones  (id_user , phone_type_id ,phone_name ,value) Values (?, ?,?, ?)', (int(id), type, name, value,))
    connection.commit   
    for item in phone_list:
        print(item)
    print('----------------')    
    answer = int(input(f"Выберете пункт меню: "))
    print()
    if answer == 1:
        add_phone_type()
    if answer == 2:
        menu()       

#отображение всего справочника
def print_table(table,i):
    sql = "SELECT * FROM " 
    sql = sql + str(table)
    connection.row_factory = sl.Row
    cursor.execute(sql)     
    connection.commit()
    results = cursor.fetchall()  

    widths = []
    columns = []
    tavnit = '|'
    separator = '+'
    for cd in cursor.description:         
        widths.append(max(0, len(cd[0])))
        columns.append(cd[0])
    for w in widths:
        tavnit += " %-"+"%s.%ss |" % (w,w)
        separator += '-'*w + '--+'
    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator) 
    if i==1:
        input(f"Нажмите Enter чтобы вернуться в меню ")
        menu()

def print_finde_user(id):
    sql = "SELECT usr.id [Указатель], usr.username as [Имя] , usr.age,pt.value [Тип номера], phn.value as [Номер] FROM Users usr, Phones phn, PhoneType pt  Where usr.id = ? and usr.id=phn.id_user and phn.phone_type_id = pt.id"
    connection.row_factory = sl.Row
    cursor.execute(sql, (int(id),))     
    connection.commit()
    results = cursor.fetchall()  

    widths = []
    columns = []
    tavnit = '|'
    separator = '+'
    for cd in cursor.description:         
        widths.append(max(0, len(cd[0])))
        columns.append(cd[0])
    for w in widths:
        tavnit += " %-"+"%s.%ss |" % (w,w)
        separator += '-'*w + '--+'
    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator) 
    print()
    answer = int(input(f"Нажмите 1, чтобы удалить или 2, чтобы вернутья в основное меню "))
    print()
    if answer == 1:
        delete_abonent(id)
    if answer == 2:
        menu()        


#Содаем БД и требуемые таблицы
connection = sl.Connection("gb.db")
connection.create_collation("NOCASE", ignore_case_collation)
connection.create_function("LOWER", 1, sqlite_lower)
cursor = connection.cursor()
cursor.execute("Select * From users")
create_db()
opearting = True

menu()

print('----------------')
print('Всего доброго!')
connection.close()
#cursor.execute("Select * From users")

#results = cursor.fetchall()

# for row in results:
#   print(row)



