z=input()
y=z.upper()
if z==y:
    print(z.lower())
else:
    if z[0]<=y[0]:
        print(z)
    else:
        print(z.title() if z[1:]==y[1:] else z)
