
key = int(input('Key: '))
text = input('Message: ')

arrays = []
for i in range(key):
    row = []
    for x in range(len(text)):
        row.append('')
    arrays.append(row)

curRow = 0
direction = 1
for i in range(len(text)):
    letter = text[i]
    arrays[curRow][i] = letter
    curRow += direction
    if (curRow > 2):
        curRow = 1
        direction = -1
    if (curRow < 0):
        curRow = 1
        direction = 1


final = ''
for row in arrays:
    for letter in row:
        final += letter

print(final)
