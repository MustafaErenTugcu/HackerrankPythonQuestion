N = int(input())
lst = []
for i in range(N):
    com=input().split()
    if com[0]==("insert"):
        lst.insert(int(com[1]),int(com[2]))
    elif com[0]==("print"):
        print(lst)
    elif com[0]==("remove"):
        lst.remove(int(com[1]))
    elif com[0]==("append"):
        lst.append(int(com[1]))
    elif com[0]==("sort"):
        lst.sort()
    elif com[0]==("pop"):
        lst.pop()
    elif com[0]==("reverse"):
        lst.reverse()
    else:
        pass