#working code 1 : problem is that we don't check if the value is in the range once we put a right input.

# answer = 63
# inputNumber = int(input())
#
# if inputNumber > 0 and inputNumber < 100:
#     if inputNumber == answer:
#         print ("Correct Answer")
#     while inputNumber - answer:
#         if answer - inputNumber < 0:
#             print ("hot")
#         elif answer - inputNumber > 0:
#             print ("cold")
#         inputNumber = int(input())
#         if inputNumber == answer:
#             print ("Correct Answer")
# else:
#     print ("Wrong Input")

# Working Code 2: Problem Solved...
answer = 63
inputNumber = int(input())

while inputNumber - answer:
    if inputNumber > 0 and inputNumber < 100:
        if answer - inputNumber < 0:
            print ("hot")
        elif answer - inputNumber > 0:
            print ("cold")
        inputNumber = int(input())
        if inputNumber == answer:
            print ("Correct Answer")
    else:
        print ("Wrong Input")
        inputNumber = int(input())
