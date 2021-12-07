import itertools
from itertools import combinations_with_replacement
from itertools import combinations


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

    def test3(self):
        for layout in (self.basegroups[int(self.noOfBaseGroups) - 2]):
            for lays in layout:
                for element in lays:
                    if element == "X":
                        print("X")
                    if element == "O":
                        print("O")

    def test2(self):
        for baseunit in self.base:
            office = 0
            atrium = 0
            for baseunitunit in baseunit:
                for baseunitunitunit in baseunitunit:
                    if baseunitunitunit == "I":
                        office += 1
                    if baseunitunitunit == "A":
                        atrium += 1
            # print(office+atrium)
            # print(office)
            # print(atrium)

    def getLayouts(self):
        self.test3()
        X = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
        allVariations = list(itertools.product(self.base, repeat=int(self.noOfBaseGroups)))
        print(allVariations[32][1])
        for layout in (self.basegroups[int(self.noOfBaseGroups) - 2]):
            for lays in layout:
                for variations in range(len(allVariations)):
                    Space = lays
                    for i in range(len(self.Space)):
                        for j in range(len(self.Space[i])):
                            if Space[i][j] == "X":
                                print("XD")
                                Space[i][j] = X
                            if Space[i][j] == "O":
                                Space[i][j] = allVariations[variations]
                self.layoutList.append(Space)
