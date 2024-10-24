COLOURS = {"WHITE": 0, "BLACK": 1}


class board:  # manages board and game
    def __init__(self):
        self.__board = [[None] * 8] * 8
        self.setup()
        #self.printBoard()

    def setup(self):
        for location in range(8):
            self.__board[0][location] = piece([6, location], 0, location)  # index 6 is 7th row of the self.__board
            print(location)
            self.printBoard()
        for location in range(8):
            self.__board[7][location] = piece([7, location], 0, location + 8)
        for location in range(8):
            self.__board[1][location] = piece([1, location], 1, location)  # index 6 is 7th row of the self.__board
        for location in range(8):
            self.__board[0][location] = piece([0, location], 1, location + 8)

    def movePiece(self, startIndex: list, endIndex: list):
        if endIndex[0] > 8 or endIndex[1] > 8:
            print("ERROR: Destination to move out of range")

        elif self.__board[endIndex[0]][endIndex[1]] is None:  # if None in dest put piece their and put old square to None
            self.__board[endIndex[0]][endIndex[1]] = self.__board[startIndex[0]][startIndex[1]]
            self.__board[startIndex[0]][startIndex[1]] = None

        elif self.__board[endIndex[0]][endIndex[1]].getColour() != self.__board[startIndex[0]][startIndex[1]].getColour():
            self.__board[endIndex[0]][endIndex[1]] = self.__board[startIndex[0]][startIndex[1]]
            self.__board[startIndex[0]][startIndex[1]] = None

    def printBoard(self):
        print()
        for row in range(8):
            print(self.__board[row])
    def checkCheck(self):
        pass


class piece:
    def __init__(self, location: list, colour: int, playerIndex: int):
        self.__location = location
        self.__colour = colour
        self.__playerIndex = playerIndex
        self.name = "piece"

    def getColour(self):
        return self.__colour

board()
