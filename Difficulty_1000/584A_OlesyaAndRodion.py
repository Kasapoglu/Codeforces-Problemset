n, t = map(int, input().split())

if t == 10:
    if n == 1:
        print(-1)
    else:
        print("1" + "0"*(n-1))
else:
    if n == 1:
        if t == 10:
            print(-1)
        else:
            print(t)
    else:
        if t > 1 and t <= 9:
            print(str(t) * n)
        else:
            if t > 9:
                if n*t > n+9:
                    print(str(t) * (n-1) + "0")
                else:
                    print(-1)
            else:
                print(-1)
