n = input('Введите n ')
s = 2
flag = 0

for degree in range(0, int(n)+1):
    if degree == 0:
        print(f"2^{degree} = 1")
    else:
        s = 1
        for i in range(1, degree+1):
            s = s*2
        if s>int(n):
            flag = 1
            break
        else:
            print(f"2^{degree} = {s}")   
    if flag == 1 :
         break        
