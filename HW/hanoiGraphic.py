def HanoiMain(layer, ColumnA, ColumnB, ColumnC):
    if layer == 1 :
        HanoiGraphic(layer, [0,0,0,0,0,layer] , [0,0,0,0,0,0]  , [0,0,0,0,0,0])
        return 0

    HanoiMain(layer - 1, ColumnA, ColumnC, ColumnB )
    HanoiGraphic(layer, [0,0,0,0,0,layer] ,  [1,1,1,1,1,1] , [0,0,0,0,0,0])
    HanoiMain(layer - 1, ColumnB, ColumnA, ColumnC)



def HanoiGraphic (layer, firstHas, secondHas, thirdHas):
    eachlayer = "\t{}\t{}\t{}\t"
    for i in range(layer): print(eachlayer.format(firstHas[i], secondHas[i], thirdHas[i]))
    print("     -----------------------\n")



HanoiMain(6, 1,2,3)
# def HanoiPath (layer, ColumnA, ColumnB, ColumnC):
#     if layer == 1 :
#         print(pathString.format(1, ColumnA, ColumnC))
#         return 0
#
#     HanoiPath(layer - 1, ColumnA, ColumnC, ColumnB)
#     print(pathString.format(layer, ColumnA, ColumnC))
#     HanoiPath(layer - 1, ColumnB, ColumnA, ColumnC)
