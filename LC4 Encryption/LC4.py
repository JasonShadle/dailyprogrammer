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

def shift(cypherChar,plainChar):
    plainPos = np.argwhere(board == plainChar)
    x = plainPos[0][0]
    plainXRow= []
    # fill in cypherXRow with current row
    for d in range(0, 6):
        plainXRow.append(board[plainPos[0][0], d])

    # shift the board row
    for c in range(0, 6):
        board[x, c] = plainXRow[(c-1)%6]

    cypherPos = np.argwhere(board == cypherChar)
    cypherYRow = []
    y = cypherPos[0][1]
    for e in range(0, 6):
        cypherYRow.append(board[e, cypherPos[0][1]])

    for b in range(0, 6):
        board[b, y] = cypherYRow[(b-1)%6]


def decypher(message):
    decypherMessage = ''
    marker = [0,0]
    for char in mInput:
        markerChar = board[marker[0], marker[1]]
        cypherCords = np.argwhere(board == char)
        plainX = (cypherCords[0][0] - marker[0]) % 6
        plainY = (cypherCords[0][1] - marker[1]) % 6
        plainText = board[plainX][plainY]
        plainCords = np.argwhere(board == plainText)
        decypherMessage += plainText
        shift(board[cypherCords[0][0], cypherCords[0][1]], board[plainCords[0][0], plainCords[0][1]])
        markerTemp = np.argwhere(board == markerChar)
        marker[0] = markerTemp[0][0]
        marker[1] = markerTemp[0][1]
    return decypherMessage

# bInput = input('What is the tile arrangement?')
# mInput = input('What is the message to decypher?')
bInput = 's2ferw_nx346ty5odiupq#lmz8ajhgcvk79b'
mInput = 'tk5j23tq94_gw9c#lhzs'

assignValues(bInput)
print(decypher(mInput))
