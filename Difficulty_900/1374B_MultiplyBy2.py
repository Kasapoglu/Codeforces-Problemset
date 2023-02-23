t = int(input())

for i in range(t):
    case = int(input())
    moves = 0
    while(case!=1):
        moves+=1
        if(case%6==0):
            case/=6
        else:
            if(case%3==0):
                case*=2
            else:
                print(-1)
                break
    else:
        print(moves)
