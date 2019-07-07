# 숫자를 입력받아, 그 숫자 만큼의 개수의 소수를 만들어내는 함수.

# 1. num 개수의 소수를 갖는 array를 return 한다.
# 2. return값이 없이, num개의 소수를 출력하기만 한다.

# numInput = int(input())
#
#
# def primeGenerator(div):
#     divarray = [2]
#     until = 1000
#     for dividend in range(2, until) :
#         mult = 1
#         for divisor in range(2, dividend):
#             mult *=  bool(dividend % divisor)
#             if mult != 0 and divisor == dividend - 1:
#                 divarray.append(dividend)
#                 break
#     return divarray
#
#
# print (primeGenerator(numInput)[numInput - 1])
#

# # 위 코드의 문제점 :
# 1) 1000까지 이내의 소수를 저장해 뒀기 때문에, 1000 넘어가는 소수에 대한 핸들링이 되지 않는다.
# 2) 이 함수는 어레이를 반환하는 함수지, 소수를 반환하는 함수가 아님.

# 아래는 수정한 코드다.

numInput = int(input())
primeArr = [2]

def primeGenerator(div):
    divarray = [2]
    until = 1000
    for dividend in range(2, until) :
        mult = 1
        for divisor in range(2, dividend):
            mult *=  bool(dividend % divisor)
            if mult != 0 and divisor == dividend - 1:
                divarray.append(dividend)
                break
    return divarray[div -1]


def primeGeneratorHeech(div):
    dividend = primeArr[len(primeArr) - 1]
    while (len(primeArr) != div ) :
        mult = 1
        for divisor in range(2, dividend):
            mult *=  bool(dividend % divisor)
            if mult != 0 and divisor == dividend - 1:
                primeArr.append(dividend)
                break
        dividend += 1
    return primeArr[div -1]



# print (primeGenerator(numInput))
print (primeGeneratorHeech(numInput))
