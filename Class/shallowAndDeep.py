origianlArr = ["a", "b", "c"]

shallowCopyArr = origianlArr
deepCopyArr = origianlArr.copy()
print(origianlArr)
print(shallowCopyArr)

shallowCopyArr[1] = "x"
print(origianlArr)
print(shallowCopyArr)
print(deepCopyArr)
