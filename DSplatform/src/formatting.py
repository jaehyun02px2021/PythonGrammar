def getNameOfFile() :
    temp =  input("type the file name: ")
    print(temp)
    return temp

def getElementSep():
    return input("type es :" )




def fileSeperator(path, elementSeperator ):
    fileString = open(path, "rt").read()
    resultArr = []
    # print(fileString)

    for line in fileString.splitlines() :
        resultArr.append(line.split(elementSeperator))
    # print(resultArr)
    return resultArr



# you can add feature using "lineSeperator"



def formatting() :
    resultArr = fileSeperator("./data/WONBON/{}.txt".format(getNameOfFile()),getElementSep())
    title = input("type the title for the formatted file: ")
    format = input("type the input element : ")
    newFile = open("./data/Formatted/{}.txt".format(title), "w")
    for dataArr in resultArr:
        for dataElement in dataArr:
            newFile.write(dataElement + format)
# erase underscore at the end of each line :
# if index == len(dataArr)
# just newFile.write(dataElement) (no format)
        newFile.write("\n")






#Reference
#for c in resultArr:
    # for l in c:
    #     newfile.write(l + ' ')
    # newfile.write("\n")

# fileSeperator(getPathOfFile(),",", "\n")

# ./data/WONBON/somefile.txt
