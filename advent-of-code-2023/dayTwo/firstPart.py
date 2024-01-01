# Define maximum values and other variables
totalRed = 12
totalGreen = 13
totalBlue = 14
finalResult = 0


# Parse the game data and return the maximum number of cubes for the game
def parseColors(inputData):
    maxRed = 0
    maxGreen = 0
    maxBlue = 0

    for gameData in inputData:
        for cubes in [cubeEntry.strip() for cubeEntry in gameData.split(',')]:
            cubeNum = int(cubes.split(' ')[0])
            cubeColor = cubes.split(' ')[1]
            match cubeColor:
                case "red":
                    if cubeNum > maxRed:
                        maxRed = cubeNum
                case "green":
                    if cubeNum > maxGreen:
                        maxGreen = cubeNum
                case "blue":
                    if cubeNum > maxBlue:
                        maxBlue = cubeNum

    return maxRed, maxGreen, maxBlue


# Read the game data and return results
with open("gameData.txt") as file:
    for line in file:
        gameID = int(line.split(':')[0].split(' ')[1].strip())
        gameCubeData = [entry.strip() for entry in line.split(':')[1].split(';')]
        redCubes, greenCubes, blueCubes = parseColors(gameCubeData)
        if redCubes <= totalRed and greenCubes <= totalGreen and blueCubes <= totalBlue:
            finalResult += gameID

print(f"The final result is {finalResult}")
