
sizeOfGroup = 16
sizeOfUnit = 25

def calculate(area,levels):
    NoOfLayouts = (int(area)/(int(sizeOfUnit)*int(sizeOfGroup)))/int(levels)
    return NoOfLayouts