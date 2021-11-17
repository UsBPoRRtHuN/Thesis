from Model import BaseGroup
from Model.BaseUnit import BaseUnit
import parseConfigs


# default értékek

class Generate:
    sizeOfGroup = 16
    sizeOfUnit = 25
    area = 8000
    levels = 4
    noOfLayouts = 10
    noOfBaseGroups = 5
    baseGroupList = []
    baseUnitList = []

    def init(self):
        self.loadConfigs(self)
        self.calculate(self)
        self.generateLayouts(self)

    def generateLayouts(self):
        self.noOfLayouts = 1

        allPossibleLayouts = 1  # Placeholder érték
        for i in range(int(self.noOfBaseGroups)):
            allPossibleLayouts *= len(self.baseUnitList)
        self.examineCompatibility(self)

    def examineCompatibility(self):
        borders = []
        finalBorders = {}
        self.getBorders(self, borders)
        self.createBorders(self, borders, finalBorders)
        print(finalBorders)

    def getBorders(self, borders):
        for i in range(len(self.baseUnitList)):
            item = []
            for j in range(len(self.baseUnitList[i])):
                if j == 0 or j == (len(self.baseUnitList[i]) - 1):
                    item.append(self.baseUnitList[i][j])
                else:
                    temp = []
                    for k in range(len(self.baseUnitList[i][j])):
                        if k == 0 or k == (len(self.baseUnitList[i][j]) - 1):
                            temp.append(self.baseUnitList[i][j][k])
                    item.append(temp)
            borders.append(item)

    def createBorders(self, borders, finalBorders):
        for i in range(len(borders)):
            left = []
            right = []

            top = [borders[i][0]]  # Első elem, ez mindig a teteje lesz a BaseGroupnak
            down = [borders[i][-1]]  # BaseGroup magasságát felhasználva megkapom az utolsó elemét
            for j in range(len(borders[i])):
                left.append(borders[i][j][0])  # bal széle
                right.append(borders[i][j][-1])  # jobb széle
            groupBorder = [top, right, down, left]
            finalBorders[i] = groupBorder

    def calculate(self):
        self.noOfBaseGroups = (int(self.area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(self.levels)

    def loadConfigs(self):
        self.baseGroupList = parseConfigs.parseBaseGroupJson()
        self.baseUnitList = parseConfigs.parseBaseUnitJson()
