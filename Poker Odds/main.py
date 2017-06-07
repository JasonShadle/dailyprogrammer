cardNumbers = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
cardSuits = ['D','S','C','H']
cardsRemaining = []

def detWinner(p1,p2,p3,p4,deck):


# populate cardsRemaining
for x in range (0, len(cardNumbers)):
    for y in range (0, len(cardSuits)):
        cardsRemaining.append(cardNumbers[x] + cardSuits[y])

# get input
flopcardsStr = input('Enter the flop:')
p1cardsStr = input('Enter Player 1 cards:')
p2cardsStr = input('Enter Player 2 cards:')
p3cardsStr = input('Enter Player 3 cards:')
p4cardsStr = input('Enter Player 4 cards:')

# convert to array
flopcards = [flopcardsStr[i:i+2] for i in range(0, len(flopcardsStr), 2)]
p1cards = [p1cardsStr[i:i+2] for i in range(0, len(p1cardsStr), 2)]
p2cards = [p2cardsStr[i:i+2] for i in range(0, len(p2cardsStr), 2)]
p3cards = [p3cardsStr[i:i+2] for i in range(0, len(p3cardsStr), 2)]
p4cards = [p4cardsStr[i:i+2] for i in range(0, len(p4cardsStr), 2)]

# delete flop/playercards from cardsRemaining
for x in range(0, len(flopcards)):
    cardsRemaining.pop(cardsRemaining.index(flopcards[x]))
for x in range(0, len(p1cards)):
    cardsRemaining.pop(cardsRemaining.index(p1cards[x]))
for x in range(0, len(p2cards)):
    cardsRemaining.pop(cardsRemaining.index(p2cards[x]))
for x in range(0, len(p3cards)):
    cardsRemaining.pop(cardsRemaining.index(p3cards[x]))
for x in range(0, len(p4cards)):
    cardsRemaining.pop(cardsRemaining.index(p4cards[x]))

