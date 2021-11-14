import json
import os
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

# TODO szebb megoldás a dictionary beolvasására
# json fájlszerkesztő

groupList = []
unitList = []

def parseBaseGroupJson():
    with open(os.getcwd() + '\\Data\\GroupConfigs.json', 'r') as groupFile:
        groupData = groupFile.read()
        group = json.loads(groupData)
        for i in range(len(group)):
            groupList.append(group[
                                  str(i + 2)])  # Mivel a legkisebb kiosztás is 2 alapegységből áll, ezért kell a +2 offset a nevezékhez
        return groupList

def parseBaseUnitJson():
    with open(os.getcwd() + '\\Data\\BaseUnitConfigs.json', 'r') as unitFile:
        unitData = unitFile.read()
        unit = json.loads(unitData)
        unitList.append(unit)
        return unitList

