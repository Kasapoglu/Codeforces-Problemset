n = int(input())
implementedProblems = 0
for i in range(n):
    P,V,T = map(int,input().split())
    total = P+V+T
    if total>1:
        implementedProblems+=1
print(implementedProblems)