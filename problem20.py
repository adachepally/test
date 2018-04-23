import math
n=math.factorial(100)
n = str(n)
sum = 0
for i in range(len(n)):
    s = int(n[i])
    sum += s

print(sum)