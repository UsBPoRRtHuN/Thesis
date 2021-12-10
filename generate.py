import itertools

from Model import BaseGroup
from Model.BaseUnit import BaseUnit
import parseConfigs
import layout


class Generate:
    # Default values
    area = 8000
    levels = 10
    noOfLayouts = 100
    noOfBaseGroups = 5
    baseGroupList = []
    baseUnitList = []
    layoutList = []
    matchingBorders = {}
    allVariations = []
    ratioMax = 0.65
    ratioMin = 0.35

    def init(self):
        self.loadConfigs(self)
        self.calculate(self)
        self.examineCompatibility(self)
        self.generateLayouts(self)
        print(self.matchingBorders)

    def getLayout(self, num):
        if not self.layoutList:
            self.init(self)
        return self.layoutList[num]

    def generateLayouts(self):
        for layouts in list(self.baseGroupList[int(self.noOfBaseGroups) - 2]):
            for variations in self.allVariations:
                helper = list(layouts)
                lay = layout.Layout()
                lay.getLayout(helper, variations)
                self.layoutList.append(lay)

    def examineCompatibility(self):
        borders = []
        finalBorders = {}
        self.matchingBorders = {}
        self.getBorders(self, borders)
        self.createBorders(self, borders, finalBorders)
        self.matchingBorders = self.compareBorders(self, finalBorders)

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
            top = {'top': [borders[i][0]]}
            down = {'down': [borders[i][-1]]}
            # Első elem, ez mindig a teteje lesz a BaseGroupnak
            # BaseGroup magasságát felhasználva megkapom az utolsó elemét
            for j in range(len(borders[i])):
                leftList.append(borders[i][j][0])  # bal széle
                rightList.append(borders[i][j][-1])  # jobb széle
            left["left"] = leftList
            right["right"] = rightList
            finalBorders[i] = top, right, down, left

    def calculate(self):
        self.noOfBaseGroups = (int(self.area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(self.levels)
        allVariations = list(itertools.product(self.baseUnitList, repeat=int(self.noOfBaseGroups)))
        allVariationsFiltered = []
        for variations in allVariations:
            I = 0
            A = 0
            for variationsvariation in variations:
                for variationvariationvariation in variationsvariation:
                    for variationvariationvariationvariation in variationvariationvariation:
                        if variationvariationvariationvariation == "I":
                            I += 1
                        if variationvariationvariationvariation == "A":
                            A += 1
            if A == 0:
                ratioA = 0
                ratioI = 1
            if I == 0:
                ratioA = 1
                ratioI = 0
            if A != 0 and I != 0:
                total = A + I
                ratioA = I / total
                ratioI = A / total
            if self.ratioMax >= ratioA >= self.ratioMin and self.ratioMax >= ratioI >= self.ratioMin:
                allVariationsFiltered.append(variations)
        self.allVariations = allVariationsFiltered
        self.noOfLayouts = len(self.allVariations)

    def loadConfigs(self):
        self.baseGroupList = parseConfigs.parseBaseGroupJson()
        self.baseUnitList = parseConfigs.parseBaseUnitJson()
