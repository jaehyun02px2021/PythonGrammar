# USing Array Example

primenumber = []
test = 2


while test < 100 :
    if len(primenumber) == 0 :
        primenumber.append(test)
    else :
        for divisor in primenumber:
            if test % divisor == 0 :
                break
            if divisor == primenumber[len(primenumber)-1] :
                primenumber.append(test)
    test += 1


print(primenumber)



for x in range(2, 100):
    if x > 3 :
        for y in range(2, x):
            if x % y == 0 :
                break
