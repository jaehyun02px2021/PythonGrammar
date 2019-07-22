import numpy as np

def getMeanJH(realResultArr):
    sum = 0
    for Num in realResultArr:
        sum += Num
    return sum/len(realResultArr)

def getMedianJH(realResultArr):
    Arr = realResultArr.copy()
    x = len(Arr)
    medianArr = []
    for Num in realResultArr:
        medianArr.append(min(realResultArr))
        realResultArr.remove(min(realResultArr))
        if len(medianArr) == len(Arr):
            break
    print(medianArr)
    # if (len(medianArr)/2) == int((len(medianArr)/2)):
    print(len(medianArr))
    if len(medianArr) % 2 == 0:
        return medianArr[(len(medianArr)/2)]
    else:
        return (medianArr[int(len((medianArr/2)))+1] + medianArr[int(len((medianArr/2)))-1])/2


def getMean(Arr):
    return np.mean(Arr)

def getMedian(Arr):
    return np.median(Arr)

def getIQR(Q1Q3Arr) :
    return Q1Q3Arr[1]  - Q1Q3Arr[0]

    # if len(Arr) % 2 != 0:
    #
    #     return
    #     # return np.sort(Arr).tolist().split(np.sort(Arr)[getMedian(Arr)])
    # else:
    #     return 345

def getQ1Q3(Arr):
    belowHalf = []
    aboveHalf = []
    median = getMedian(Arr)

    for num in Arr:
        if (num < median) :
            belowHalf.append(num)
        elif (num > median) :
            aboveHalf.append(num)

    return [ getMedian(aboveHalf) , getMedian(belowHalf) ]


def getOutLier(Arr) :
    for num in Arr:
        if num < 1.5*

def getSTDEV(Arr):
    return np.std(Arr)

def getRange(Arr):
    return 1

def getMax(Arr):
    return 1

def getMin(Arr):
    return 1
# ======================

def Normalize(Arr) :
    NormalizedArr = []
    for element in Arr:
        NormalizedArr.append((element-getMean(Arr))/getSTDEV(Arr))
    return NormalizedArr
