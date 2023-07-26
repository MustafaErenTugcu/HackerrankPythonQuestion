from collections import defaultdict
d = defaultdict(list)

n= int(input("Enter a parameter of A : "))

for i in range(n):
    letter = input("Enter a letter :  ")
    d["GroupA"].append(letter)
m = int(input("Enter a parameter of B : "))

for i in range(m):
    letter = input("Enter a letter : ")
    d["GroupB"].append(letter)

for k,v in d.items():
    print(v)





"""print(d)
print(d["GroupA"])
print(d["GroupB"])
"""