import sys

# Split file content into lists
with open(sys.argv[1]) as file:
    seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation = file.read().split('\n\n')

print(seedToSoil)
