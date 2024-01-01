import re
import sys

finalCount = 0

# Custom function for converting the spelled number to a string
def wordToNum(inputString):
    match inputString:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9


regexNumNames = re.compile('(?=(one|two|three|four|five|six|seven|eight|nine|\d))')

# Parse the words, convert them into integers and combine them at the end
with open(sys.argv[1]) as file:
    for line in file:
        matches = [x if x.isdigit() else wordToNum(x) for x in regexNumNames.findall(line.strip())]
        finalCount += int(str(matches[0]) + str(matches[-1]))

print(f"The final answer is {finalCount}")

