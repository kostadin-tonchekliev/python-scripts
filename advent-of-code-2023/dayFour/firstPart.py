import sys

totalScore = 0

# Verify if the winning number exists in the ticket numbers and return the score
def verifyNumbers(winningNums, ticketNums):
    flag = False
    ticketScore = 0

    for number in winningNums:
        if number in ticketNums:
            if not flag:
                ticketScore = 1
                flag = True
            elif flag:
                ticketScore *= 2

    return ticketScore


# Go through the tickets and return the final number
with open(sys.argv[1]) as file:
    for entry in file:
        winningNumbers, ticketNumbers = [nums.strip().split(' ') for nums in entry.split(':')[1].replace('  ', ' ').split('|')]
        totalScore += verifyNumbers(winningNumbers, ticketNumbers)

print(f"The final score is {totalScore}")
