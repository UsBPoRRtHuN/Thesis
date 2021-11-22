import random

class Layout:
    Space = []
    def __init__(self, baseUnitList):
        self.baseUnitList = baseUnitList



    def getLayouts(self):
        X = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
        self.Space = [[X,X,self.baseUnitList[random.randint(0,1)],X,self.baseUnitList[random.randint(0,1)]], [X,self.baseUnitList[random.randint(0,1)],X,X,X], [self.baseUnitList[random.randint(0,1)],X,X,X,self.baseUnitList[random.randint(0,1)]], [X,self.baseUnitList[random.randint(0,1)],X,X,X], [X,X,self.baseUnitList[random.randint(0,1)],X,X]]
