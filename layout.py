class Layout:
    Space = []
    layoutList = []

    def __init__(self, baseUnitList, matchingBorders, noOfLayouts, baseGrouplist, noOfBaseGroups):
        self.base = baseUnitList
        self.borders = matchingBorders
        self.layouts = noOfLayouts
        self.basegroups = baseGrouplist
        self.noOfBaseGroups = noOfBaseGroups

    def giveLayoutList(self):
        return self.layoutList

    def getLayouts(self):
        O = [self.base[0][1], self.base[1][0], self.base[0][1], self.base[1][0]]
        X = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
        for lay in self.basegroups:
            self.Space = lay
            print(len(lay))
            for i in range(len(self.Space)):
                for j in range(len(self.Space[i])):
                    if self.Space[i][j] == "X":
                        self.Space[i][j] = X
                    if self.Space[i][j] == "O":
                        self.Space[i][j] = O
                self.layoutList.append(self.Space)