n = input()
almostLucky = [4,7,47,74,447,474,477,774,747]
isAlmostLucky = "NO"
for i in n:
    if i == "4" or i == "7":
        pass
    else:
        break
else:
    isAlmostLucky = "YES"
 
if isAlmostLucky=="YES":
    print(isAlmostLucky)
else:
    for i in almostLucky:
        if int(n)%i == 0:
            print("YES")
            break
    else:
        print(isAlmostLucky)
