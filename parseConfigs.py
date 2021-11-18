import json
import os
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

#TODO json fájlszerkesztő

groupList = []
unitList = []

def parseBaseGroupJson():
    with open(os.getcwd() + '\\Data\\GroupConfigs.json', 'r') as groupFile:
        groupData = groupFile.read()
        group = json.loads(groupData)
        for key in group:
            groupList.append(group[key])
        return groupList

def parseBaseUnitJson():
    with open(os.getcwd() + '\\Data\\BaseUnitConfigs.json', 'r') as unitFile:
        unitData = unitFile.read()
        unit = json.loads(unitData)
        for key in unit:
            unitList.append(unit[key])
        return unitList

