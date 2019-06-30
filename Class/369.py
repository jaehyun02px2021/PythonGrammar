# this code is bullshit

# limit = int(input())
#
# if limit < 0 or limit > 100:
#     print ("Wrong input")
#
# while limit > 0 and limit < 100:
#     print ("ADfadj")

limit = int(input())



def Seperate (num):
    stringNum = str(num)
    numArray = []
    for i in range(len(stringNum)):
        numArray.append(stringNum[i])
    return numArray

def Check (anyArray):
    count = 0
    for x in anyArray:
        if int(x) % 3 == 0  and int(x) != 0:
            count += 1
    return count


if limit < 0 or limit > 10000000:
    print ("Wrong input")
else:
    for x in range(1, limit + 1):
        b = Check(Seperate(x))
        if b == 0:
            print (x)
        else:
            for x in range (b):
                print ("짝", end = '')
            print('')
