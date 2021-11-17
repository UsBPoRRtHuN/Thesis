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
        self.getBorders(self, borders)

    def getBorders(self, borders):
        item = []
        for i in range(len(self.baseUnitList)):
            for j in range(len(self.baseUnitList[i])):
                if j == 0 or j == (len(self.baseUnitList[i]) - 1):
                    item.append(self.baseUnitList[i][j])
                else:
                    for k in range(len(self.baseUnitList[i][j])):
                        if k == 0 or k == (len(self.baseUnitList[i][j]) - 1):
                            item.append(self.baseUnitList[i][j][k])
        print(type(item[0]))

    def calculate(self):
        self.noOfBaseGroups = (int(self.area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(self.levels)
        print(self.noOfBaseGroups)
        print(self.levels)

    def loadConfigs(self):
        self.baseGroupList = parseConfigs.parseBaseGroupJson()
        self.baseUnitList = parseConfigs.parseBaseUnitJson()
