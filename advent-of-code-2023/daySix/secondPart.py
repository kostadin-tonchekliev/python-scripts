# Basically the same as first part but without the loops or dictionary
time = 54708275
distance = 239114212951253

buttonHoldingTime = 0
timeTraveling = 0
totalTime = 0
traveledDistance = 0
winningAttempts = []

while buttonHoldingTime < time:
    buttonHoldingTime += 1
    timeTraveling = distance / buttonHoldingTime
    totalTime = buttonHoldingTime + timeTraveling
    if totalTime < time:
        winningAttempts.append(buttonHoldingTime)

print(f"The final answer is {len(winningAttempts)}")
