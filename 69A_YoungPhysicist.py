n = int(input())
totalForces={"x":0,"y":0,"z":0}

for i in range(n):
    x , y , z = map(int,input().split()) 
    totalForces["x"]+=x
    totalForces["y"]+=y
    totalForces["z"]+=z

for i in totalForces.values():
    if i!=0:
        print("NO")
        break
else:
    print("YES")
