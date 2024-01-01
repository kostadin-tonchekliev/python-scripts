# Build a dictionary with all race data
races = {
    1: {
        'time': 54,
        'distance': 239,
        'winning_attempts': []
    },
    2: {
        'time': 70,
        'distance': 1142,
        'winning_attempts': []
    },
    3: {
        'time': 82,
        'distance': 1295,
        'winning_attempts': []
    },
    4: {
        'time': 75,
        'distance': 1253,
        'winning_attempts': []
    }
}

# Loop through the races
for race in races:
    time = races[race]['time']
    distance = races[race]['distance']

    buttonHoldingTime = 0
    timeTraveling = 0
    totalTime = 0
    traveledDistance = 0
    winningAttempts = []

    while buttonHoldingTime < time:
        buttonHoldingTime += 1
        # Quick maths
        timeTraveling = distance / buttonHoldingTime
        totalTime = buttonHoldingTime + timeTraveling
        if totalTime < time:
            races[race]['winning_attempts'].append(buttonHoldingTime)

# Multiply the total number of winning attempts for each race
totalWinningAttempts = len(races[1]['winning_attempts']) * len(races[2]['winning_attempts']) * len(races[3]['winning_attempts']) * len(races[4]['winning_attempts'])

print(f"The final answer is {totalWinningAttempts}")
