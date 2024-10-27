COLOURS = {"WHITE": 0, "BLACK": 1}


class board:  # manages board and game
    def __init__(self):
        self.__board = [[None for column in range(8)] for rows in range(8)]
        self.setup()

    def setup(self):
        for row in range(0, 2):
            for column in range(8):
                self.__board[row][column] = piece((row, column), 0, (row, column))
        for row in range(6, 8):  # index 6 is 7th row of the self.__board
            for column in range(8):
                self.__board[row][column] = piece((row, column), 0, (row, column))
        self.printBoard()

    def movePiece(self, startIndex: list, endIndex: list):
        if endIndex[0] > 8 or endIndex[1] > 8:
            print("ERROR: Destination to move out of range")

        elif self.__board[endIndex[0]][
            endIndex[1]] is None:  # if None in dest put piece their and put old square to None
            self.__board[endIndex[0]][endIndex[1]] = self.__board[startIndex[0]][startIndex[1]]
            self.__board[startIndex[0]][startIndex[1]] = None

        elif self.__board[endIndex[0]][endIndex[1]].getColour() != self.__board[startIndex[0]][
            startIndex[1]].getColour():
            self.__board[endIndex[0]][endIndex[1]] = self.__board[startIndex[0]][startIndex[1]]
            self.__board[startIndex[0]][startIndex[1]] = None

        else:
            print("Attempted move was onto own colour")

    def __validateMove(self, piece: object, move: list | tuple):
        if not move[0] > 8 and not move[0] < 0 and not move [1] > 8 and move[1] < 8:
            currentLocation = self.piece.getLocation()
            locationChangeBy = [currentLocation[0] - move[0], currentLocation[0] - move[0]]
            # need to work out some sort of iteration that uses the math cba rn
    def printBoard(self):
        print()
        for row in range(8):
            items = []
            for item in range(8):
                if self.__board[row][item] == None:
                    items.append(None)
                else:
                    try:
                        items.append(self.__board[row][item].name)
                    except:
                        items.append("UNKNOWN ITEM ON BOARD")
            print(items)

    def checkCheck(self):
        pass


class piece:
    def __init__(self, location: list, colour: int, playerIndex: int):
        self.__location = location
        self.__colour = colour
        self.__playerIndex = playerIndex
        self.name = "piece"
        self._maxMovesForward = 1
        self._maxMovesBackward = 1
        self._maxMovesSideways = 1
        self._maxMovesDiagonal = 1

    def getColour(self):
        return self.__colour

    def getLocation(self):
        return self.__location

    def setLocation(self, newLoc: list | tuple):
        self.__location = newLoc


board()
