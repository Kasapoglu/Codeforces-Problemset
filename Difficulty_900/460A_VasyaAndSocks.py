n , m = map(int,input().split())
days = 0

while n!=0:
    
    days+=1
    
    if days%m==0:
        pass
    else:
        n-=1

print(days)

