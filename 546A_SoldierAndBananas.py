k,n,w = map(int,input().split())
totalCost = ((w * (w+1))/2)*k
borrowMoney = int(totalCost-n)
print(borrowMoney if borrowMoney>0 else 0)