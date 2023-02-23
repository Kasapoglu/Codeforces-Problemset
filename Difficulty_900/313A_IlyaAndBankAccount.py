balance=input()
if int(balance)>=0:
    print(balance)
else:
    x = int(balance[:-1])
    y = int(balance[:-2]+balance[-1])
    print(max(int(x),int(y)))
