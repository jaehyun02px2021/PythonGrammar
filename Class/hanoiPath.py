pathString = "{} : {} \t -> {}"


def HanoiPath (layer, ColumnA, ColumnB, ColumnC):
    if layer == 1 :
        print(pathString.format(1, ColumnA, ColumnC))
        return 0

    HanoiPath(layer - 1, ColumnA, ColumnC, ColumnB)
    print(pathString.format(layer, ColumnA, ColumnC))
    HanoiPath(layer - 1, ColumnB, ColumnA, ColumnC)


HanoiPath(8, "FIRST", "SECOND", "THIRD")
