n, k = map(int, input().split())
lastOddNum = (n + 1) // 2
if k <= lastOddNum:
    print((k * 2) - 1)
else:
    print((k - lastOddNum) * 2)