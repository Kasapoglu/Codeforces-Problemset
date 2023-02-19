vowels = ["a","o","y","e","u","i"]
string = input().lower()
result = str()

for i in string:
    if i in vowels:
        pass
    else:
        result+=("."+i)
        
print(result)
