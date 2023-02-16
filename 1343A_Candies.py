t = int(input())
 
for i in range(t):
    
    case = int(input())
    
    k = 2
    
    while case / ((2**k)-1) != int(case / ((2**k)-1)):
        k+=1
    
    print(int(case / ((2**k)-1)))

