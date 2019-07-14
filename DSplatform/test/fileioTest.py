# Reference :
# http://aikorea.org/cs231n/python-numpy-tutorial/
# https://www.numpy.org/
import numpy as np

sample = open("./data/sample.txt", "rt")

# print(sample.read())

# abc = sample.read()
# defg = abc.splitlines()

defg = sample.read().splitlines()
resultArr =[]

for x in defg:
    resultArr.append(x.split())

 # following makes error

# sampleArr = sample.read().splitlines()
#
#
#
# for idx, str in sampleArr :
#     print(sampleArr[idx])
#     sampleArr[idx] = str.split()

print(resultArr)

newfile = open("./data/result.txt", "w")

for c in resultArr:
    for l in c:
        newfile.write(l + ' ')
    newfile.write("\n")

# 숙제 1)
# 어떤 기능을 갖고 있을지 구상해온다.
# 숙제 2)
# Split 할 Specifier를 생각해온다.
