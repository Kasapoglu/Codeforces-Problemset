n , m , a = map(int,input().split())

x = n//a + 1
y = m//a + 1

if n/a > n//a:
    neededStonesLength = n//a + 1
else:
    neededStonesLength = n//a
    
if m/a > m//a:
    neededStonesWidth = m//a + 1
else:
    neededStonesWidth = m//a

print(neededStonesLength*neededStonesWidth)
