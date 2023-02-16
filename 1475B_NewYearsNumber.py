t = int(input())
 
for i in range(t):
    case = int(input())
    
    if case<2020:
        print("NO")
    else:
        a = case // 2020
        b = case % 2020
        if b==0:
            print("YES")
        else:
            print("YES" if b<=a else "NO")
