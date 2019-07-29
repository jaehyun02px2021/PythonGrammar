import src.statisticsFunction as sF

def getNameOfFile1() :
    temp = input("type the first file name: ")
    return temp

def getNameOfFile2() :
    temp = input("type the second file name: ")
    return temp

def getElementSep1():
    temp = input("type the element seperator for the first file: ")
    return temp

def getElementSep2():
    temp = input("type the element seperator for the second file: ")
    return temp

def fileSeperator1(fileName1, elementSeperator1):
    resultArr = []
    realResultArr = []
    for line in open("./data/Formatted/{}.txt".format(fileName1, "rt")).read().splitlines():
        resultArr.append(line.split(elementSeperator1))

    for strNum in resultArr[0]:
        realResultArr.append(float(strNum))
    return realResultArr

def fileSeperator2(fileName2, elementSeperator2):
    resultArr = []
    realResultArr = []
    for line in open("./data/Formatted/{}.txt".format(fileName2, "rt")).read().splitlines():
        resultArr.append(line.split(elementSeperator2))

    for strNum in resultArr[0]:
        realResultArr.append(float(strNum))
    return realResultArr

def LeastSquare():
    ArrX = fileSeperator1(getNameOfFile1(), getElementSep1())
    ArrY = fileSeperator2(getNameOfFile2(), getElementSep2())
    MeanX = sF.getMean(ArrX)
    MeanY = sF.getMean(ArrY)
    STDEVX = sF.getSTDEV(ArrX)
    STDEVY = sF.getSTDEV(ArrY)
    R_Value = 0

    for i in range(len(ArrX)):
        R_Value += ((ArrX[i] - MeanX)/STDEVX)*(((ArrY[i] - MeanY)/STDEVY))

    R_Value *= (1/(len(ArrX)-1))

    command = ""

    while command != "stop" :
        mode = int(input("""choose explanatory variable :
        1 for first array
        2 for second array"""))

        if mode == 1 :
            b = R_Value*(STDEVY/STDEVX)
            a = MeanY - b*MeanX
        elif mode == 2 :
            b = R_Value*(STDEVX/STDEVY)
            a = MeanX - b*MeanY
        else :
            print("invalid input. try again")
            continue

        print("r - value:{}".format(R_Value))
        print("least square regression line: \ny = {} + {}x".format(a, b))
        print("Prediction : ")

        explanatoryValue = ""

        while explanatoryValue != "stop" :
            explanatoryValue = input("type sample explanatory value: ")
            responseValue = b *  int(explanatoryValue) + a
            print( "Tada ! result is {}".format(responseValue))


    # for x in firstArr:
    #     d = ((x-sF.getMean(firstArr))/sF.getSTDEV(firstArr))
    # for y in secondArr:
    #     l = ((y-sF.getMean(secondArr))/sf.getSTDEV(secondArr))
    #
