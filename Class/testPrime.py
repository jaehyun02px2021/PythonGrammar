
limit = int(input())
print(2)
for x in range (2, limit):
    for y in range (2, x):
        if x % y == 0:
            break
        if y == x - 1:

            print(x)
