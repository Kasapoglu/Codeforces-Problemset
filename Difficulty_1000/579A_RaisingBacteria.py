def division(y):
    global totalBacteria,x
    
    if y+totalBacteria > x:
        return (y/2)
    else:
        return division(y*2) 


x = int(input())
bacteria = 0
totalBacteria=0

while totalBacteria != x:
    bacteria+=1
    totalBacteria += division(1)

print(bacteria)
