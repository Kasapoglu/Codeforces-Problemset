s,n = map(int,input().split())
dragons={}

for i in range(n):
    x,y = map(int,input().split())
    dragons[x] = y + dragons.get(x,0)

for i in range(len(dragons.keys())):
    tempDragon = min(dragons.keys())
    
    if tempDragon < s:
        s+=dragons[tempDragon]
        del dragons[tempDragon]
    else:
        print("NO")
        break
else:
    print("YES")
