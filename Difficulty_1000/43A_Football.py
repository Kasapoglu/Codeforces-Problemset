n=int(input())
scores={}
for i in range(n):
    goal=input()
    scores[goal] = 1 + scores.get(goal,0)

for key,value in scores.items():
    if value==max(scores.values()):
        print(key)
        break
