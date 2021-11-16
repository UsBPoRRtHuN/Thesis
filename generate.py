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


    def calculate(self):
        self.noOfBaseGroups = (int(self.area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(self.levels)
        print(self.noOfBaseGroups)
        print(self.levels)

    def loadConfigs(self):
        self.baseGroupList = parseConfigs.parseBaseGroupJson()
        self.baseUnitList = parseConfigs.parseBaseUnitJson()



