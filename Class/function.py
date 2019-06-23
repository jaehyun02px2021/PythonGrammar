# variable = int(input())
# def f (x):
#     return x**2 + 3
#
# print (f(variable))


# def factorial (x):
#     if x == 1 : return 1
#     else : return x * factorial(x-1)
#
# print(factorial(5))


# def fibonacci (x):
#     if x == 1 : return 0
#     elif x == 2 : return 1
#     else : return fibonacci(x-2) + fibonacci(x-1)
#
# print(fibonacci(45))


hanoiNum = int(input())

def testinput (x) :
    if x < 1 : return "Wrong Input"
    else: return Hanoi(x)

def Hanoi (x):
    if x == 1 : return 1
    else : return 2 * Hanoi (x-1) + 1

print(testinput(hanoiNum))
