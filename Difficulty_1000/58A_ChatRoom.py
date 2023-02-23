hello = ["h","e","l","l","o"]
copy = hello.copy()
result = []

s = input()

for i in s:
    
    if copy==[]:
        break

    if i==copy[0]:
        result.append(copy[0])
        copy.remove(copy[0])

print("YES" if result == hello else "NO")
