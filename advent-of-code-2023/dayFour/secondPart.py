import sys

# Create a variable for the final result and a dictionary for the cards and their data
totalCards = 0
allCards = {}
"""
{
    'ticketId': {
        'score' : int,
        'copies': int
    }
}
"""

# Return the matches
def returnMatches(winningNums, ticketNums):
    matches = 0

    for number in winningNums:
        if number in ticketNums:
            matches += 1

    return matches


# Go through the cards and build the ticket dictionary
with open(sys.argv[1]) as file:
    for entry in file:
        ticketId = int(entry.split(':')[0].split(' ')[-1].strip())
        winningNumbers, ticketNumbers = [nums.strip().split(' ') for nums in entry.split(':')[1].replace('  ', ' ').split('|')]
        score = returnMatches(winningNumbers, ticketNumbers)
        allCards[ticketId] = {'score': score, 'copies': 1}

# Go through the ticket dictionary and add the copies to each one
for card in allCards:
    # Verify if there are any matches in the card
    cardScore = allCards[card]['score']
    if cardScore > 0:
        for copy in range(allCards[card]['copies']):
            for x in range(cardScore):
                counter = x + 1
                allCards[card + counter]['copies'] += 1

# Loop through the ticket dictionary again so that we can get the final number based on the copies
for card in allCards:
    totalCards += allCards[card]['copies']

print(f"The final score is {totalCards}")
