n,m = map(int,input().split())
tasks = list(map(int,input().split()))

pointer = 1
timeUnits = 0

for i in tasks:
    
    if pointer<i:
        timeUnits+=(i-pointer)
        
    elif pointer==i:
        pass
    
    else:
        timeUnits+=((n-pointer)+i)
    
    pointer=i
            
print(timeUnits)
