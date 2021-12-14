import copy
import itertools

from Model import BaseGroup
from Model.BaseUnit import BaseUnit
import parseConfigs
import layout


class Generate:
    # Default values
    area = 9000
    levels = 5
    noOfLayouts = 100
    noOfBaseGroups = 5
    baseGroupList = []
    baseUnitList = []
    layoutList = []
    matchingBorders = {}
    allVariations = []
    ratioMax = 100
    ratioMin = 0
    maxOfficeLength = 4

    def init(self):
        self.loadConfigs(self)
        self.calculate(self)
        self.generateLayouts(self)

    def getLayout(self, num):
        if not self.layoutList:
            self.init(self)
        return self.layoutList[num]

    def generateLayouts(self):
        for layouts in list(self.baseGroupList[int(self.noOfBaseGroups) - 2]):
            for variations in self.allVariations:
                horizontal = False
                helper = copy.deepcopy(layouts)
                m = helper
                rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
                for rows in rez:
                    if rows.count("O") > 1:
                        horizontal = True
                if horizontal is True:
                    horizontalApproved = self.checkHorizontal(self, layouts, variations)
                    if horizontalApproved:
                        lay = layout.Layout()
                        lay.getLayout(layouts, horizontalApproved)
                        self.layoutList.append(lay)

        self.noOfLayouts = len(self.layoutList)

    def checkRatio(self, allVariations):
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
        return allVariationsFiltered

    def calculate(self):
        self.noOfBaseGroups = (int(self.area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(self.levels)
        allVariations = list(itertools.product(self.baseUnitList, repeat=int(self.noOfBaseGroups)))
        allVariationsFiltered = self.checkRatio(self, allVariations)
        allVariationsFilteredEx = self.checkExteriorSides(self, allVariationsFiltered)
        allVariationsFilteredExAtr = self.checkAtrium(self, allVariationsFilteredEx)
        allVariationsFilteredExAtrInt = self.checkInteriorOfficeLength(self, allVariationsFilteredExAtr)
        self.allVariations = allVariationsFilteredExAtrInt
        self.noOfLayouts = len(self.allVariations)

    def checkAtrium(self, allVariationsFiltered):
        newList = []
        for variations in allVariationsFiltered:
            OfficeComparer = []
            lastRow = []
            helper = []
            atriumBefore = False
            atriumAfter = False
            atriumLast = False
            atriumBlocked = False
            for groups in variations:
                for groupelements in groups:
                    helper.append(groupelements)
            lastRow = helper[-1]
            for i in range(len(groups)):
                OfficeComparer.append("I")
            for element in lastRow:
                if element == "A":
                    atriumLast = True
            for groups in helper:
                for groupelements in groups:
                    if groupelements == "A":
                        atriumBefore = True
                if groups == OfficeComparer and (atriumBefore is True or atriumLast is True):
                    atriumBlocked = True
            if atriumBlocked is not True:
                newList.append(variations)
        return newList

    def checkExteriorSides(self, allVariationsFiltered):
        allVariationsExteriorFiltered = []
        for variations in allVariationsFiltered:
            valid = False
            for variationsvariations in variations:
                for variationsvariationsvariations in variationsvariations:
                    if variationsvariationsvariations[0] == "I" or variationsvariationsvariations[-1] == "I":
                        valid = True
            if valid == False:
                pass
            if valid is True:
                allVariationsExteriorFiltered.append(variations)
        return allVariationsExteriorFiltered

    def checkInteriorOfficeLength(self, allVariationsFiltered):
        newList = []
        grouphelper = []
        helper = []
        collection = []
        for variations in allVariationsFiltered:
            valid = True
            grouphelper = []
            for groups in variations:
                for groupelements in groups:
                    grouphelper.append(groupelements[1:-1])
            for i in range((len(groupelements[1:-1]))):
                list = []
                for j in range(len(grouphelper)):
                    list.append(grouphelper[j][i])
                offices = 0
                for elements in list:
                    if elements == "I":
                        offices += 1
                        if offices > self.maxOfficeLength:
                            valid = False
                    else:
                        offices = 0
            if valid is True:
                newList.append(variations)
        return newList

    def checkHorizontal(self, layouts, variations):
        index = 0
        dict = {}
        helper = copy.deepcopy(layouts)
        allCounter = 0
        counterList = []
        counterListList = []
        transposedVariation = []
        wrapper = []
        innerOfficeLength = True
        atriumOK = True
        for i in range(len(layouts)):
            dict[i] = []
            for j in range(len(layouts[i])):
                if layouts[i][j] == "O":
                    dict[i].append(index)
                    index += 1
                else:
                    dict[i].append("X")
        m = dict
        rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        for rows in rez:
            counter = 0
            for elements in rows:
                if isinstance(elements, int):
                    counterList.append(elements)
                    counter += 1
            if counter == 0:
                pass
            if counter == 1:
                counterList.remove(counterList[-1])
            if counter > 1:
                counterListList.append(counterList)
                counterList = []
        for items in counterListList:
            transposedVariation = []
            for index in items:
                m = variations[index]
                rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
                transposedVariation.append(rez)
            atriumOK = self.checkHorizontalAtrium(self,transposedVariation)
            if atriumOK is True:
                return variations

    def checkHorizontalAtrium(self, variations):
        OfficeComparer = []
        lastRow = []
        helper = []
        atriumBefore = False
        atriumAfter = False
        atriumLast = False
        atriumOK = True

        for groups in variations:
            for groupelements in groups:
                helper.append(groupelements)
        lastRow = helper[-1]
        for i in range(len(groups)):
            OfficeComparer.append("I")
        for element in lastRow:
            if element == "A":
                atriumLast = True
        for groups in helper:
            for groupelements in groups:
                if groupelements == "A":
                    atriumBefore = True
            if groups == OfficeComparer and (atriumBefore is True or atriumLast is True):
                atriumOK = False
        return atriumOK

    def loadConfigs(self):
        self.baseGroupList = parseConfigs.parseBaseGroupJson()
        self.baseUnitList = parseConfigs.parseBaseUnitJson()
