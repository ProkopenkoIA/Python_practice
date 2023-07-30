import random

x = random.randint(0,1000)
y = random.randint(0,1000)

flag = 0

s = x+y
p = x*y

print("Загадано: x = {} and y = {}".format(x,y))

for i in range(0, 1001):    
    for j in range(0, 1001):
        if i+j == s and i*j == p: 
            flag = 1           
            break
    if flag == 1:
        break        
print("Ответ: x = {} and y = {}".format(i,j))        
