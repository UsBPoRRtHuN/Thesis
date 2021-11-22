from Model import BaseGroup
from Model.BaseUnit import BaseUnit
import parseConfigs
import layout


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
        layoutList = []
        self.loadConfigs(self)
        self.calculate(self)
        layoutList = self.generateLayouts(self)
        return layoutList

    def generateLayouts(self):
        layoutList = []
        self.noOfLayouts = 1
        matchingBorders = self.examineCompatibility(self)
        currentNoOfGroupLayoutLength = (len(self.baseGroupList[int(self.noOfBaseGroups - 2)]))
        allPossibleLayouts = (len(matchingBorders) * currentNoOfGroupLayoutLength) + (
                    len(self.baseUnitList) * currentNoOfGroupLayoutLength)  # ez még vszeg hibás érték
        for i in range(allPossibleLayouts):
            lay = layout.Layout(self.baseUnitList)
            lay.getLayouts()
            layoutList.append(lay)
        return layoutList

    def examineCompatibility(self):
        borders = []
        finalBorders = {}
        matchingBorders = {}
        self.getBorders(self, borders)
        self.createBorders(self, borders, finalBorders)
        matchingBorders = self.compareBorders(self, finalBorders)
        return matchingBorders

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
                        for res in range(len((finalBorders))):
                            if int(key) < int(res):  # önmagánál kisebbet már ne vizsgáljon
                                for comparingPos in range(len(finalBorders[res])):
                                    for comparingBorder in (finalBorders[res][comparingPos]):
                                        if finalBorders[key][pos][border] == finalBorders[res][comparingPos][
                                            comparingBorder] and finalBorders[res] is not finalBorders[
                                            key]:  # önmagát ne vizsgálja
                                            i += 1
                                            # print("A " + str(key) + ". groupunit" + str(finalBorders[key][pos]) + " oldala megegyezik a " + str(res) + str(finalBorders[res][comparingPos]) + "oldalával")
                                            matchingBorders[i] = [str(key), finalBorders[key][pos]], [str(res),
                                                                                                      finalBorders[res][
                                                                                                          comparingPos]]
                    except (ValueError, IndexError, KeyError):
                        pass
        return matchingBorders

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
