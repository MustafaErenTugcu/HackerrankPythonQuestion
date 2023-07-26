x = int(input())
y = int(input())
z = int(input())
n = int(input())


m = [[xa,ya,za] for xa in range(x+1) for ya in range(y+1) for za in range(z+1) if xa+ya+za != n  ] 

print(m)
