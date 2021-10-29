import json

def parseJson():
    with open('C:\\Users\\Takacs.Peter\\Desktop\\Thesis\\Data\\GroupConfigs.json', 'r') as myfile:
        data = myfile.read()
        obj = json.loads(data)