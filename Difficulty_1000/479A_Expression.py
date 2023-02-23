num=[]

for i in range(3):
    num.append(int(input()))

a=num[0]
b=num[1]
c=num[2]
print(max(a+b+c, a+b*c, (a+b)*c, a*b+c, a*(b+c), a*b*c))
