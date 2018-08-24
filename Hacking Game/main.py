import random, math
words = []
dictionary = []
difficulty = input('Difficulty (1-5)?')
lettersInWord = int(difficulty) * 2 + 2
numOfWords = int(difficulty) * 2 + 2
file = open('enable1.txt', 'r')
guesses = 5
correctLetters = 0

for line in file:
    word = line.strip()
    dictionary.append(word)

while len(words) < numOfWords:
    location = math.floor(random.random() * 172820)
    if len(dictionary[location]) == lettersInWord:
        words.append(dictionary[location])

for word in words:
    print(word)

correctWord = words[math.floor(len(words) * random.random())]

while guesses > 1:
    guesses -= 1
    correctLetters = 0
    userGuess = (input('Guess (' + str(guesses) + ' left)?'))
    for x in range(0, lettersInWord):
        if correctWord[x] == userGuess[x]:
            correctLetters += 1
    if correctLetters == lettersInWord:
        input('You win! Press Enter to quit.')
        quit()
    print(str(correctLetters) + '/' + str(lettersInWord) + ' correct.')

input('You lost, press Enter to exit.')


