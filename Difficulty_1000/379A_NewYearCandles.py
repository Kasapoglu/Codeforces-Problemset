a,b=map(int,input().split())

wentOutCandles = a
numOfNewCandle = 0

while wentOutCandles>=b:
    newCandle = wentOutCandles//b
    remainder = wentOutCandles%b
    
    numOfNewCandle += newCandle
    wentOutCandles = remainder+newCandle

print(a + numOfNewCandle)
