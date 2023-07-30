

n = input('Введите n ')
value = [0,1]
pull = ''

for coin in range(1, int(n)+1):
    c = input(f"введите сторону монеты {coin} ")
    if int(c) not in value:
        print('Ошибка: Значение должно быть 0 или 1')
    pull = pull + c
print(pull)
sum = 0
for i in pull:
    if int(i) == 1:
        sum+=1

answer = 0
if sum != 0 or sum != n:
    compare = int(n) - sum
    if compare>sum:
        answer = sum
    else:
        answer = compare

print('Минимальное количество переворотов: '+str(answer))            

    
