import random

numberOfH = 0
numberOfB = 0
ComputerScore = 0
UserScore = 0


def computerSMART (rsc, RSboundary, SPboundary) :
    if rsc >= RSboundary and rsc < SPboundary:
        print ("Computer Help")
        return 1
    elif rsc < RSboundary and rsc >= 0:
        print ("computer Betrayal")
        return 2
    else:
        print ("computer Help")
        return 1


def winorlose (userinput, computerinput):

    global ComputerScore, UserScore
    if computerinput == 1 and userinput == 1:
        ComputerScore += 2
        UserScore += 2
        print ("Computer Score =")
        print (ComputerScore)
        print ("User Score =")
        print (UserScore)
        return "Computer +2, User +2"
    elif computerinput == 2 and userinput == 2:
        print ("Computer Score =")
        print (ComputerScore)
        print ("User Score =")
        print (UserScore)
        return "Computer +0, User +0"
    elif computerinput == 1 and userinput == 2:
        ComputerScore -= 1
        UserScore += 3
        print ("Computer Score =")
        print (ComputerScore)
        print ("User Score =")
        print (UserScore)
        return "Computer -1, User +3"
    elif computerinput == 2 and userinput == 1:
        ComputerScore += 3
        UserScore -= 1
        print ("Computer Score =")
        print (ComputerScore)
        print ("User Score =")
        print (UserScore)
        return "Computer +3, User -1"



while(1) :
    choice = int(input())

    if choice != 1 and choice != 2:
        print ("Wrong Input")
    else:
        if choice == 1:
            print ("user help")
            numberOfH += 1
        elif choice == 2:
            print ("user betrayal")
            numberOfB += 1


    rsc = random.random() * 2
    RSboundary =  2 * numberOfH / (numberOfH + numberOfB)
    SPboundary = 2 - 2 * numberOfB / (numberOfH + numberOfB)

    print (winorlose(choice, computerSMART(rsc, RSboundary, SPboundary)))
