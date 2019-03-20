def getsum():
    total = 0
    for i in range(1,101):
        total = total + i
    return pow(total,2)

def getsquare():
    total = 0
    for i in range(1,101):
        s = pow(i,2)
        total = total + s
    return total

sum = getsum()
square = getsquare()
print(sum - square)