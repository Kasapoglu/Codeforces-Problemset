numberOfCoins=input()
coins = list(map(int,input().split()))
sortedList = sorted(coins,reverse=True)
totalCost = sum(coins)
takenCoins=0
takenCoinsValue=0
for i in range(len(coins)):
    
    takenCoinsValue+=sortedList[i]
    takenCoins+=1
    
    if takenCoinsValue>(totalCost/2):
        break

print(takenCoins)