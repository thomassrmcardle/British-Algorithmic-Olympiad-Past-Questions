w = int(input('W: '))

n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

k = int(input('k: '))

cardinals = []

def processRow(n):
    cardinalRow = []
    for i in range(n):
        cardinalRow.append(i)
    cardinals.append(cardinalRow)

[processRow(n) for n in [n1, n2, n3]]

def iterate():
    pass