stack = list()
a = int(input())

for i in range(a):
    x = input()
    try:
        c,d = x.split()
        d = int(d)
    except:
        c = x
    if c == "push" : 
        stack.append(d)
    elif c == "top" :
        if len(stack) == 0 : print("-1")
        else: print(stack[len(stack)-1])
    elif c == "size" :
        print(len(stack))
    elif c == "empty" :
        if len(stack) == 0 : print("1")
        else : print("0")
    elif c == "pop" :
        if len(stack)==0 :
            print("-1")
        else :
            print(stack[len(stack)-1])
            stack.pop()