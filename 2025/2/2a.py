w = int(input('W: '))

n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

k = int(input('k: '))

cardinals = []

class Cardinal:
    def __init__(self, cords, score):
        self.cords = cords
        self.score = score

    def getSiblings(self):
        siblings = []
        for row in cardinals:
            for c in row:
                location = c.getLocation()
                if (location[0] - location[0] == -1) or (location[0] - location[0] == 1):
                    siblings.append(c)
                elif (location[1] - location[1] == -1) or (location[1] - location[1] == 1):
                    siblings.append(c)
        return siblings
        

    def check_over(self):
        if self.score < 3:
            # Add k check
            self.score = max(self.score-1, 0)#
        else:
            siblings = self.getSiblings()
            applicable = 0
            for c in siblings:
                if c.getScore() == 3:
                    applicable += 1
            self.score = min(self.score+applicable, 3)

    def getLocation(self):
        return self.cords

    def getScore(self):
        return self.score

rowIndex = 0
def processRow(n):
    cardinalRow = []
    for i in range(n):
        cardinalRow.append(Cardinal([i, rowIndex], 0)) # [Radial Coordinate,  Popularity rating]
    rowIndex += 1
    cardinals.append(cardinalRow)

[processRow(n) for n in [n1, n2, n3]]

def iterate():
    for row in cardinals:
        for c in row:
            c.check_over()