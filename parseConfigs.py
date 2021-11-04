import json
import os
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

# TODO szebb megoldás a dictionary beolvasására

objectList = []


def parseJson():
    with open(os.getcwd() + '\\Data\\GroupConfigs.json', 'r') as groupFile:
        data = groupFile.read()
        group = json.loads(data)
        for i in range(len(group)):
            objectList.append(group[
                                  str(i + 2)])  # Mivel a legkisebb kiosztás is 2 alapegységből áll, ezért kell a +2 offset a nevezékhez
        return objectList