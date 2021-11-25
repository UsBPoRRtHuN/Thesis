class Layout:
    Space = []
    layoutList = []

    def __init__(self, baseUnitList, matchingBorders, noOfLayouts, iterator, baseGrouplist, noOfBaseGroups):
        self.base = baseUnitList
        self.borders = matchingBorders
        self.layouts = noOfLayouts
        self.iterator = iterator
        self.basegroups = baseGrouplist
        self.noOfBaseGroups = noOfBaseGroups

    def getLayouts(self):
        O = [self.base[0][1], self.base[1][0], self.base[0][1], self.base[1][0]]
        X = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
        self.Space = self.basegroups[int(self.noOfBaseGroups-2)][3]
        for i in range(len(self.Space)):
            for j in range(len(self.Space[i])):
                if self.Space[i][j] == "X":
                    self.Space[i][j] = X
                if self.Space[i][j] == "O":
                    self.Space[i][j] = O
