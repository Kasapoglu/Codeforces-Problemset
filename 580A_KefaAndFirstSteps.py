n = input()
numbers = list(map(int,input().split()))
nonDecreasing = []
subSegmentNum = 1

if len(numbers)<2:
    print(1)
else:   
    for i in range(len(numbers)-1):
        x = numbers[i]
        y = numbers[i+1]
        if x <= y:
            subSegmentNum+=1
            if y==numbers[-1]:
                nonDecreasing.append(subSegmentNum)
        else:
            nonDecreasing.append(subSegmentNum)
            subSegmentNum=1


    print(1 if nonDecreasing is [] else max(nonDecreasing))
