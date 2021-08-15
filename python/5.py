lst = []
for i in range(2,50):
    c = 0
    for j in range(2,i):
        if (i%j) == 0:
            c=c+1
            break

    if(c==0 and i!=1):
            lst.append(i)
            
rows = 4
lst = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
copy = lst

space=(2*rows)-2

count = 0

for i in range(0,rows+1):
    for j in range(0,space):
        print(end=" ")
    space = space-1
    
    for j in range(0,i+1):
        count = count+1
        if(j!=0):
            print(lst[count-1], end =" ")
        else:
            print(lst[count-1], end =" ")
    print("\n")