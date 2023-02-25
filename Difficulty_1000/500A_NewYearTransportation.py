n,t = map(int,input().split())
a = list(map(int,input().split()))

portals=[]
for i in range(1,n):
    if i ==1:
        portals.append((i,i+a[i-1]))
    else:
        if portals[-1][1]==i:
            portals.append((i,i+a[i-1]))

for i in portals:
    if i[1]==t:
        print("YES")
        break
else:
    print("NO")
