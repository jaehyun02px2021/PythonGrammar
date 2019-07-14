# Hello = "Hello World"
#
# print (Hello)
# Hello = "안녕하세요"
# print (Hello)


# a = int(input())
# b = int(input())
# c = int(input())
#
# ResultPlus = (-b+(b ** 2 - 4 * a * c)**(1/2))/(2 * a)
# ResultMinus = (-b-(b ** 2 - 4 * a * c)**(1/2))/(2 * a)
# print (ResultPlus)
# print (ResultMinus)


n = int(input())

if n > 100 or n < 1:
    print ("Wrong Input")
else:
    print ("Right input")
    if n % 2 != 0:
        print ("Weird")
    elif 2 <= n and n <= 5:
        print ("Not Weird")
    elif  n >= 6 and n <= 20:
        print ("Weird")
    else:
        print ("Not Weird")
