stonesNum = input()
stonesColor = list(input())
counter = 0

if len(stonesColor)==1:
    pass
else:    
    for i in range(len(stonesColor)-1):
        x = stonesColor[i]
        y = stonesColor[i+1]
        if x==y:
            counter+=1
        else:
            pass
print(counter)
