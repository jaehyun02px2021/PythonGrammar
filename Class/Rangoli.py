# size = int(input())
#
# if size < 0 or size > 26
#     print ("Wrong Input")
#
# # 오늘의 숙제 힌트!
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# 1. 가운데 줄을 만드는 함수를 작성한다.
# 2. 사이즈 값에 따라서, 한 줄의 길이를 저장하는 변수가 있어야 한다. 4n -3
# 3. 가운데 줄을 만드는 함수를 확장해서, 파라미터 1개를 추가해, 가운데에서 몇번쨰 떨어진 줄이라도 만들수 있도록 한다.
# 4. for 문을 사용해서, 함수에 적절한 파라미터를 반복시켜서, 최종적인 랭골리를 그린다.

# source : https://code.sololearn.com/cUNVT83ei1BD/#py
# built-in function chr(param) returns a single  character
# according to  the ascii code table.

def print_rangoli(size):
    width  = size*4-3
    string = ''

    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
        string = ''

    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))

# if __name__ == '__main__':
n = int(input())
print_rangoli(n)
