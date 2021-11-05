from Model import BaseGroup
from Model.BaseUnit import BaseUnit
import parseConfigs

# default értékek


sizeOfGroup = 16
sizeOfUnit = 25
area = 8000
levels = 4
noOfLayouts = 20

def calculate():
    NoOfLayouts = (int(area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(levels)
    Group = BaseGroup.BaseGroup()
    return NoOfLayouts

def parseConfig():
    list = parseConfigs.parseJson()