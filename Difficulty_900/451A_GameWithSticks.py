n , m = map(int,input().split())
intersections = n*m
winner = "Malvika"
while intersections>=1:
    intersections-=(n+m-1)
    n-=1
    m-=1
    if winner == "Akshat":
        winner = "Malvika"
    else:
        winner = "Akshat"
print(winner)
