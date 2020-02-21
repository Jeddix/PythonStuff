import datetime
import random

def printStats(playedSongs, perc):
    print(str(datetime.datetime.now().time()) + ";" + str(playedSongs) + ";" + str(round(perc, 2)))

numberOfSongs = 8226
playedSongs = [0] * numberOfSongs

numberOfPlayedSongs = 0
counter = 0

while numberOfPlayedSongs < numberOfSongs:
    randIndex = random.randrange(numberOfSongs)

    if playedSongs[randIndex] == 0:
        counter += 1
        playedSongs[randIndex] = 1

    numberOfPlayedSongs = sum(playedSongs)
    percentage = numberOfPlayedSongs * 100 / numberOfSongs

    if counter == 50:
        counter = 0
        printStats(numberOfPlayedSongs, percentage)

printStats(numberOfPlayedSongs, percentage)

