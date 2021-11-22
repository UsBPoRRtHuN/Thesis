class Layout:
    Space = []
    def __init__(self, baseUnitList):
        self.baseUnitList = baseUnitList



    def getLayouts(self):
        X = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
        self.Space = [[X,X,self.baseUnitList[0],X,self.baseUnitList[1]], [X,self.baseUnitList[0],X,X,X], [X,X,X,X,X], [X,X,X,X,X], [X,X,X,X,X]]
