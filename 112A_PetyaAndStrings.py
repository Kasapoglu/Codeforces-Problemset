string_1 = input()
string_2 = input()

if string_1.lower() > string_2.lower():
    print(1)
elif string_1.lower() < string_2.lower():
    print(-1)  
else:
    print(0)