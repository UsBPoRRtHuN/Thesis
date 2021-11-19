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
        self.compareBorders(self, finalBorders)

    def compareBorders(self, finalBorders):
        temp = list(finalBorders)
        matchingBorders = {}
        i = -1
        for key in finalBorders:
            try:
                res = temp[temp.index(key) + 1]
            except (ValueError, IndexError):
                res = None
            for pos in range(len(finalBorders[key])):
                for border in (finalBorders[key][pos]):
                    try:
                        for comparingPos in range(len(finalBorders[res])):
                            for comparingBorder in (finalBorders[res][comparingPos]):
                                if finalBorders[key][pos][border] == finalBorders[res][comparingPos][comparingBorder]:
                                    i += 1
                                    print("A " + str(key) + ". groupunit" + str(
                                        finalBorders[key][pos]) + " oldala megegyezik a " + str(res) + str(
                                        finalBorders[res][comparingPos]) + "oldalával")
                                    matchingBorders[i] = [str(key), finalBorders[key][pos]], [str(res),
                                                                                              finalBorders[res][
                                                                                                  comparingPos]]
                    except (ValueError, IndexError, KeyError):
                        print("")
        print(matchingBorders)

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
            leftList = []
            rightList = []
            left = {}
            right = {}
            top = {}
            down = {}
            top["top"] = [borders[i][0]]  # Első elem, ez mindig a teteje lesz a BaseGroupnak
            down["down"] = [borders[i][-1]]  # BaseGroup magasságát felhasználva megkapom az utolsó elemét
            for j in range(len(borders[i])):
                leftList.append(borders[i][j][0])  # bal széle
                rightList.append(borders[i][j][-1])  # jobb széle
            left["left"] = leftList
            right["right"] = rightList
            finalBorders[i] = top, right, down, left

    def calculate(self):
        self.noOfBaseGroups = (int(self.area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(self.levels)

    def loadConfigs(self):
        self.baseGroupList = parseConfigs.parseBaseGroupJson()
        self.baseUnitList = parseConfigs.parseBaseUnitJson()
