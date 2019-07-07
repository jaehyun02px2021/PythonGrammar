# import random
#
# def winorlose (userinput, computerinput):
#     dif = computerinput - userinput
#     if dif == 0
#         return "draw"
#     elif dif == 1 or dif == -2
#         return "user wins"
#     else
#         return "computer wins"

import random

numberOfR = 0
numberOfS = 0
numberOfP = 0

def computerSMART (rsc, RSboundary, SPboundary) :
    print(RSboundary)
    print(SPboundary)
    if rsc < RSboundary and rsc >= 0:
        print ("computer Paper")
        return 3
    elif rsc >= RSboundary and rsc < SPboundary:
        print ("computer Rock")
        return 1
    else:
        print ("computer Scissors")
        return 2


def winorlose (userinput, computerinput):
    dif = computerinput - userinput
    if dif == 0:
        return "Draw"
    if dif == 1:
        return "Computer Loses"
    if dif == 2:
        return "Computer Wins"
    if dif == -1:
        return "Computer Wins"
    if dif == -2:
        return "Computer Loses"

while(1) :
    choice = int(input())


    if choice != 1 and choice != 2 and choice != 3:
        print ("Wrong Input")
    else:
        if choice == 1:
            print ("user rock")
            numberOfR += 1
        elif choice == 2:
            print ("user scissors")
            numberOfS += 1
        else:
            print ("user paper")
            numberOfP += 1

    rsc = random.random() * 3
    RSboundary =  3 * numberOfR / (numberOfP +  numberOfR + numberOfS)
    SPboundary = 3 - 3 * numberOfP / (numberOfP +  numberOfR + numberOfS)

    print (winorlose(choice, computerSMART(rsc, RSboundary, SPboundary)))

## 오늘의 숙제 :
# 3개의  case만으로 승부 논리를 만들 수 있는지 연구해몬다.
# 그리고 그 논리에 따라서 winorloseSMART 함수를 다시 만든다.

## 오늘의 숙제 2:
#  array에 1,2,3 을 넣고, 유저 인풋이 들어올 때 마다 해당 인풋을 넣어서, 해당 배열에서 랜덤원소를 가져오게 한다ㅣ.
# https://wikidocs.net/79

## 오늘의 숙제 3 :
# 게임이론을 위와 같이 머신러닝으로 만들자.
