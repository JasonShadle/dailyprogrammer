import numpy as np

tiles = ['#','_','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']
values = {}
board = np.zeros((6,6), dtype=str)

def assignValues(boardInput):

    # populate values dictionary
    for a in range(0, len(tiles)):
        # assign values to the dictionary for looking up the vectors
        values[tiles[a]] = [a % 6, int(a / 6)]

    # populate board with initial state
    charPos = 0
    for char in boardInput:
        board[int(charPos / 6)][charPos % 6] = char
        charPos += 1

def shift(xRowNum, yRowNum):
    yRow = []
    xRow = []
    for y in range(0, 6):
        yRow.append(board[yRowNum, y])

    for a in range(0, 6):
        board[yRowNum, a] = yRow[a - 1 % 6]

    for b in range(0, 6):
        xRow.append(board[b, xRowNum])

    for c in range(0, 6):
        board[c, xRowNum] = xRow[c - 1 % 6]

def decypher(message):
    markerLoc = [0,0]
    decypherMessage = ''

    for char in message:
        markerLetter = board[markerLoc[0] % 6, markerLoc[1] % 6]
        markerValue = tuple(values[markerLetter])

        encryptedChar = char
        encryptedCharLoc = np.argwhere(board == encryptedChar)
        encryptedValue = tuple(values[encryptedChar])

        plainTextXLoc = (encryptedCharLoc[0,1] - markerValue[0]) % 6
        plainTextYLoc = (encryptedCharLoc[0, 0] - markerValue[1]) % 6
        plainTextChar = board[plainTextYLoc, plainTextXLoc]

        decypherMessage += plainTextChar

        shift(encryptedCharLoc[0,1], plainTextYLoc)

        newMarkerLoc = np.argwhere(markerLetter == board)
        markerLoc[0] = newMarkerLoc[0][0]
        markerLoc[1] = newMarkerLoc[0][1]

        markerLoc[0] += encryptedValue[1]
        markerLoc[1] += encryptedValue[0]

    print(decypherMessage)







# bInput = input('What is the tile arrangement?')
# mInput = input('What is the message to decypher?')
boardInput = 's2ferw_nx346ty5odiupq#lmz8ajhgcvk79b'
encryptInput = 'tk5j23tq94_gw9c#lhzs'

assignValues(boardInput)
decypher(encryptInput)

