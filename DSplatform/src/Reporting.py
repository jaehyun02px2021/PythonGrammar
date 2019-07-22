import src.statisticsFunction as sF

def getNameOfFile() :
    temp = input("type the file name: ")
    return temp

def getElementSep(fileName):
    return open("./data/Formatted/{}.txt".format(fileName, "rt")).read(1)

def fileSeperator(elementSeperator, fileName):
    resultArr = []
    realResultArr = []
    for line in open("./data/Formatted/{}.txt".format(fileName, "rt")).read().splitlines():
        resultArr.append(line.split(elementSeperator))

    for strNum in resultArr[1]:
        realResultArr.append(int(strNum))
    return realResultArr



ReportForm = '''
+++ Lovely JH Report +++

<<Original Data Report >>

Mean : {}
Median : {}
Maximum : {}
Minimun : {}
Range : {}
STDEV : {}
IQR : {}
Outliers : {}

-------------------------
<<Normalized Data Report>>

Mean : {}
Median : {}
Maximum : {}
Minimun : {}
Range : {}
STDEV : {}
IQR : {}
Outliers : {}

'''


def Reporting():
    name = getNameOfFile()
    Arr = (fileSeperator(getElementSep(name), name))
    Nor = sF.Normalize(Arr)
    # print("Original Data: {}".format((fileSeperator(getElementSep(name), name))))
    # print("Normalized Data: {}".format(sF.Normalize(fileSeperator(getElementSep(name), name))))
    print(ReportForm.format(
    sF.getMean(Arr),
    sF.getMedian(Arr),
    sF.getMax(Arr),
    sF.getMin(Arr),
    sF.getRange(Arr),
    sF.getSTDEV(Arr),
    sF.getIQR(getQ1Q3(Arr)),
    sF.getOutLier(Arr),
    sF.getMean(Nor),
    sF.getMedian(Nor),
    sF.getMax(Nor),
    sF.getMin(Nor),
    sF.getRange(Nor),
    sF.getSTDEV(Nor),
    sF.getIQR(getQ1Q3(Nor)),
    sF.getOutLier(Nor)
    ))
