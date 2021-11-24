import random


class Layout:
    Space = []
    layoutList = []

    def __init__(self, baseUnitList, matchingBorders, noOfLayouts,iterator,baseGrouplist):
        self.base = baseUnitList
        self.borders= matchingBorders
        self.layouts = noOfLayouts
        self.iterator = iterator
        self.basegroups = baseGrouplist

    def getLayouts(self):
        X = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
        self.Space = [[X,X,X,X,X],[X,X,X,X,X],[X,X,X,X,X],[X,X,X,X,X],[X,X,X,X,X]]
        print(self.basegroups[0])