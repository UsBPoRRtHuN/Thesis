import copy
class Layout:
    Space = []
    X = (["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"])

    def test2(self):
        for baseunit in self.base:
            office = 0
            atrium = 0
            for baseunitunit in baseunit:
                for baseunitunitunit in baseunitunit:
                    if baseunitunitunit == "I":
                        office += 1
                    if baseunitunitunit == "A":
                        atrium += 1
            # print(office+atrium)
            # print(office)
            # print(atrium)

    def getLayout(self, layout, variation):
        self.Space = copy.deepcopy(layout)
        var = 0
        for i in range(len(self.Space)):
            for j in range(len(self.Space[i])):
                if self.Space[i][j] == "X":
                    self.Space[i][j] = self.X
                if self.Space[i][j] == "O":
                    self.Space[i][j] = variation[var]
                    var += 1
        return self.Space
