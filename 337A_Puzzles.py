n,m = map(int,input().split())
puzzles = sorted(list(map(int,input().split())))
 
chosenPuzzles ={}
for i in range(len(puzzles)):
    if len(puzzles[i:n+i]) < n:
        break
    x = puzzles[i:n+i]
    chosenPuzzles[x[-1]-x[0]]=x
print(min(chosenPuzzles.keys()))
