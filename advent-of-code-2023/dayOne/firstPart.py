# Variables used throughout the script
allWords = []
finalAnswer = 0

# Add all words into a list
with open("words.txt") as file:
    for line in file:
        allWords.append(line.strip('\n'))

# Loop through the words and parse them
for word in allWords:
    numArray = []
    for character in word:
        # Check if the character is a number and add it to an array
        if character.isnumeric():
            numArray.append(character)

    # Filter out words without any numbers in them
    if len(numArray) > 0:
        firstNum = numArray[0]
        lastNum = numArray[-1]
        finalAnswer += int(str(firstNum) + str(lastNum))

print(f"The final answer is {finalAnswer}")

