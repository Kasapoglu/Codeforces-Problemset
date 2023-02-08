columnNum = 0
rowNum = 0
for index,i in enumerate (range(5)):
    rows=list(map(int,input().split()))
    for index2,j in enumerate(rows):
        if j==1:
            rowNum = index+1
            columnNum = index2+1
            break
            
print(abs(3-columnNum)+abs(3-rowNum))