num = 0
next = 3

while num < 10000:
    isPrime = True
    for i in range(2, next):
        if next % i == 0:
            isPrime = False
    if isPrime:
        #print (num," : ", next)
        num = num + 1

    next = next+1
print(next-1)