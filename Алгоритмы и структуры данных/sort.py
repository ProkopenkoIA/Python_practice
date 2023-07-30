# Сортировка кучей

def heap (numbers, heap_size, root_index):
    
    largest = root_index
    lvalue = rvalue = 0
    lvalue = 2*root_index+1
    rvalue = 2*root_index+2

    if (lvalue<heap_size and numbers[lvalue]>numbers[largest]):
        largest = lvalue
    
    if (rvalue<heap_size and numbers[rvalue]>numbers[largest]):          
        largest = rvalue    

     

    if largest!= root_index:
        tmp =  numbers[root_index]
        numbers[root_index] = numbers[largest] 
        numbers[largest] =tmp
        heap (numbers, heap_size, largest)
    #print(numbers)

def sort():
    length = len(numbers)
    root = int(length/2-1)
    while root>=0:
        heap(numbers,length,root)  
        root-=1 

    length-=1

    while length>=0:        
        tmp =  numbers[0]
        numbers[0] = numbers[length] 
        numbers[length] =tmp
        heap(numbers,length,0) 
        length-=1

numbers = [2,4,3,5,1]

sort()
print(numbers)        




