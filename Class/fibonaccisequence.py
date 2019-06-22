# 0 1 1 2
prev1 = 0
prev2 = 1
fibbo = 0
fibboarray = []


while fibbo < 100 :
    prev1 = prev2
    prev2 = fibbo
    print(fibbo)
    fibbo = prev1  + prev2
    fibboarray.append(fibbo)

pre1 = 0
pre2 = 1
x2 = 0


for  x in range(3987) :
    if x2 > 100 :
        break
    pre1 = pre2
    pre2 = x2
    print(x2)
    x2 = pre1 + pre2


print(fibboarray)
