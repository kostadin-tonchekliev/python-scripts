import sys

objectList = []

with open(sys.argv[1], 'r') as file:
    for line in file:
        objectList.append([singleChar for singleChar in line.strip()])

print(objectList[1][0])