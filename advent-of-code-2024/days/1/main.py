def _smartDiff(numOne: int, numTwo: int) -> int:
    total = 0

    if numOne > numTwo:
        total = numOne - numTwo
    else:
        total = numTwo - numOne

    return total


def test():
    print("[+] Starting part - test!")

    listA = []
    listB = []
    totalCount = 0

    with open('days/1/example.txt') as file:
        for line in file:
            line = line.strip().split(' ')
            listA.append(int(line[0]))
            listB.append(int(line[-1]))

    listA.sort()
    listB.sort()

    for listPosition in range(0, len(listA)):
        charA = listA[listPosition]
        charB = listB[listPosition]
        # print(f"Comparing {charA} and {charB}. Count: {smartDiff(charA, charB)}") # Uncomment for debug
        totalCount += _smartDiff(charA, charB)

    print(f"Total: {totalCount}")


def partOne():
    print("[+] Starting part - one!")

    listA = []
    listB = []
    totalCount = 0

    with open('days/1/puzzle_input.txt') as file:
        for line in file:
            line = line.strip().split(' ')
            listA.append(int(line[0]))
            listB.append(int(line[-1]))

    listA.sort()
    listB.sort()

    for listPosition in range(0, len(listA)):
        charA = listA[listPosition]
        charB = listB[listPosition]
        # print(f"Comparing {charA} and {charB}. Count: {smartDiff(charA, charB)}") # Uncomment for debug
        totalCount += _smartDiff(charA, charB)

    print(f"Total: {totalCount}")


def partTwo():
    print("[+] Starting part - two!")

    listA = []
    listB = []
    totalCount = 0

    with open('days/1/puzzle_input.txt') as file:
        for line in file:
            line = line.strip().split(' ')
            listA.append(int(line[0]))
            listB.append(int(line[-1]))

    for number in listA:
        # print(f"{number} appears {listB.count(number)} of times") # Uncomment for debug
        totalCount += number * listB.count(number)

    print(f"Total: {totalCount}")


def main():
    test()
    partOne()
    partTwo()

