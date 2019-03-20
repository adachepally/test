sum = 0
a = 1
b = 1
while b < 4000000:
    num  = a + b
    if num % 2 == 0:
        sum += num
    a = b
    b = num
print(sum)