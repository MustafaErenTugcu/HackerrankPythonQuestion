number = int(input())
s = set()
sum = 0
for i in range(number):
    country = input()
    s.add(country)

for i in s:
    sum += 1 
print(sum)