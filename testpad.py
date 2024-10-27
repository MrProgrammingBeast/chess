twoDList = [[1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 11.9],
            [12, 14, 15, 16, 17, 18]]

print(twoDList[0][5])
print(twoDList[2][0])
print(twoDList[1][3])
print(twoDList[0][0])
print(twoDList)

def printBoard(list):
    print()
    for row in range(8):
        items = []
        for item in range(8):
            items.append(list[row][item])