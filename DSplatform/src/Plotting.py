import matplotlib.pyplot as plt
import src.LeastSquare as LS
import src.Reporting as RP


def Plotting():
    choose = int(input("""which do you wish to plot:
    1 for box plot (single variable)
    2 for scatter plot (double variable)"""))

    if choose == 1:
        FileName = RP.getNameOfFile()
        Arr = RP.fileSeperator(RP.getElementSep(FileName), FileName)
        plt.boxplot(Arr)
        plt.show()
    elif choose == 2:
        ArrX = LS.fileSeperator1(LS.getNameOfFile1(), LS.getElementSep1())
        ArrY = LS.fileSeperator2(LS.getNameOfFile2(), LS.getElementSep2())
        mode = int(input("""choose explanatory variable :
        1 for first array
        2 for second array"""))
        if mode == 1:
            plt.scatter(ArrX, ArrY)
        elif mode == 2:
            plt.scatter(ArrY, ArrX)
        else:
            print("invalid input")
        plt.show()
    else:
        print("invalid input")
