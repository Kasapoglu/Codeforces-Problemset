t = int(input())

for i in range(t):
    
    case = int(input())
    
    if case<=2:
        print("NO")
    
    else:
        if case%2==1:
            print("YES")
    
        else:
            while case%2==0:
                case=case/2
                if case==2:
                    print("NO")
                    break
            else:
                print("YES")
