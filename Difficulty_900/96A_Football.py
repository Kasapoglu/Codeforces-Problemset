numbers=input()
counter=1

for i in range(len(numbers)-1):
    x=numbers[i]
    y=numbers[i+1]
        
    if x==y:
        counter+=1
    else:
        counter=1
        
    if counter==7:
        print("YES")
        break
        
else:
    print("NO")
