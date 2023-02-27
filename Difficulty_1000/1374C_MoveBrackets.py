t = int(input())

for i in range(t):
    
    n=int(input())
    s=list(input())
    copyofS= s.copy()
    
    isOpen=False
    openBracket=0
    move=0
    
    for i in range(len(s)):
        
        if isOpen==False and copyofS[i]==(")"):
            s.append(s.pop(i))
            move+=1
            
        elif isOpen==False and copyofS[i]==("("):
            isOpen=True
            openBracket=1
        
        elif isOpen==True and copyofS[i]==("("):
            openBracket+=1
        
        elif isOpen==True and copyofS[i]==(")"):
            openBracket-=1
            if openBracket==0:
                isOpen=False
        
    print(move)
