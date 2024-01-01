import sys

finalResult = 0
cards = [
    ['A', 13],
    ['K', 12],
    ['Q', 11],
    ['J', 10],
    ['T', 9],
    ['9', 8],
    ['8', 7],
    ['7', 6],
    ['6', 5],
    ['5', 4],
    ['4', 3],
    ['3', 2],
    ['2', 1]
]
handDictionary = {}
"""
    'hand': {
        'strength': int,
        'bid': int,
        'rank', int
    }
"""

def getType(inputString) -> int:
    totalMatches = []
    inputList = [character for character in inputString]

    # Loop through the cards and check how many times they exist in the string
    for card in cards:
        cardMatch = inputList.count(card[0])
        if cardMatch > 0:
            totalMatches.append(cardMatch)

    totalMatches.sort(reverse=True)

    # The only two cases where we need the first match
    if totalMatches[0] == 5:
        currentHandStrength = 7
    elif totalMatches[0] == 4:
        currentHandStrength = 6

    # The remaining cases where we need either 2 or 3 matches. The last two are a bit excessive but wanted to be as descriptive as possible
    if totalMatches[0] == 3 and totalMatches[1] == 2:
        currentHandStrength = 5
    elif totalMatches[0] == 3 and totalMatches[1] == 1 and totalMatches[2] == 1:
        currentHandStrength = 4
    elif totalMatches[0] == 2 and totalMatches[1] == 2 and totalMatches[2] == 1:
        currentHandStrength = 3
    elif totalMatches[0] == 2 and totalMatches[1] == 1 and totalMatches[2] == 1 and totalMatches[3] == 1:
        currentHandStrength = 2
    elif totalMatches[0] == 1 and totalMatches[1] == 1 and totalMatches[2] == 1 and totalMatches[3] == 1 and totalMatches[4] == 1:
        currentHandStrength = 1

    return currentHandStrength

def findMatches(inputStr) -> list:
    localMatches = []
    for handEntry in handDictionary:
        if handDictionary[handEntry]['strength'] == inputStr:
            localMatches.append(handEntry)

    return localMatches

def convertString(inputValue):
    if type(inputValue) == str:
        singleConvertedHand = []
        for singleChar in inputValue:
            for possibleCard in cards:
                updatedCard = singleChar.replace(possibleCard[0], str(possibleCard[1]))
                if updatedCard != singleChar:
                    break
            singleConvertedHand.append(int(updatedCard))
        return singleConvertedHand
    elif type(inputValue) == list:
        singleReconstructedHand = ""
        for entry in inputValue:
            for possibleCard in cards:
                updatedCard = str(entry).replace(str(possibleCard[1]), possibleCard[0])
                if updatedCard != str(entry):
                    break
            singleReconstructedHand += updatedCard
        return singleReconstructedHand

def sortMultipleMatches(matchList) -> list:
    convertedList = []
    reconvertedList = []
    # Convert each card into a list with numbers for easier comparison
    for card in matchList:
        convertedList.append(convertString(card))

    convertedList = sorted(convertedList, reverse=True)

    for miniList in convertedList:
        reconvertedList.append(convertString(miniList))

    return reconvertedList


# Build a dictionary with all hands
with open(sys.argv[1], 'r') as file:
    for line in file:
        hand, bid = line.strip().split(' ')
        handDictionary[hand] = {'strength': getType(hand), 'bid': int(bid), 'rank': 0}

# Sort the dictionary based on the hand strength
handDictionary = dict(sorted(handDictionary.items(), reverse=True, key=lambda item: item[1]['strength']))
numHands = len(handDictionary)

allCurrentStrengths = [singleStrength['strength'] for singleStrength in handDictionary.values()]
sortedCurrentStrengths = list(set(allCurrentStrengths))
sortedCurrentStrengths.sort(reverse=True)

for strength in sortedCurrentStrengths:
    if allCurrentStrengths.count(strength) > 1:
        multipleMatches = findMatches(strength)
        multipleMatches = sortMultipleMatches(multipleMatches)
        for entry in multipleMatches:
            handDictionary[entry]['rank'] = numHands
            numHands -= 1

    else:
        singleMatch = findMatches(strength)
        handDictionary[singleMatch[0]]['rank'] = numHands
        numHands -= 1

for singleHand in handDictionary:
    finalResult += handDictionary[singleHand]['bid'] * handDictionary[singleHand]['rank']

print(f"The final result is {finalResult}")