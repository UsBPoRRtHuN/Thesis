from Model import BaseGroup
from Model.BaseUnit import BaseUnit
# default értékek


sizeOfGroup = 16
sizeOfUnit = 25


def calculate(area, levels):
    NoOfLayouts = (int(area) / (int(BaseUnit.size) * int(BaseGroup.groupSize))) / int(levels)
    Group = BaseGroup.BaseGroup()
    print(int(Group.size))

    return NoOfLayouts
