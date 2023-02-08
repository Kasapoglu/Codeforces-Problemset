n = int(input())
finalValue = 0
for i in range(n):
    statement = input()
    if "+" in statement :
        finalValue+=1
    else:
        finalValue-=1
print(finalValue)