def getNameOfQuestion():
    return input("enter the name of the question file:")






def SurveyInput():
    questionFile = open("./data/Questions/{}.txt".format(getNameOfQuestion()), "rt")
    questionArr = questionFile.read().splitlines()
    answerArr = []
    newFile = open("./data/SURVEY/{}.txt".format(input("enter the name of the result file:")), "w")
    while input("Survey Starts. Press anykey to proceed (s terminates the survey): ") != "s" :
        temp = []
        for question in questionArr:
            print(question)
            temp.append(input())
        answerArr.append(temp)
    for answerlist in answerArr:
        for answers in answerlist:
            newFile.write(answers + "_")
        newFile.write("\n")
