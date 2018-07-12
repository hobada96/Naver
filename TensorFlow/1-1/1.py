a,b,s = map(int,input().split())
if(s == 0) : 
    if(a == 0 and b == 0) : print("YES")
    else : print("NO")
else :
    if a == 0 or b == 0:
        if a == 0 and b != 0 :
            if s % b == 0 : print("YES")
            else : print("NO")
        elif(b == 0 and a != 0) :
            if s % a == 0 : print("YES")
            else : print("NO")
        else : print("NO")
    elif a == 1 or b == 1:
        if s != 1 : print("YES")
        else : print("NO")
    else :
        count = 0
        for n in range(int(s/a)-1):
            if(s-(n+1)*a)%b == 0 : count = count+1
        if count > 0 : print("YES")
        else : print("NO")