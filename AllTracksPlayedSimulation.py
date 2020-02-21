import datetime
import random

def printStats(playtime, playedSongs, perc):
    print(str(round(playtime)) + ";" + str(playedSongs) + ";" + str(round(perc, 2)))

numberOfSongs = 8226
playlistLengthInMinutes = 33846
playedSongs = [0] * numberOfSongs

numberOfPlayedSongs = 0
counter = 0
playtime = 0

averageSongDuration = playlistLengthInMinutes / numberOfSongs

while numberOfPlayedSongs < numberOfSongs:
    randIndex = random.randrange(numberOfSongs)
    playtime += averageSongDuration

    if playedSongs[randIndex] == 0:
        counter += 1
        playedSongs[randIndex] = 1

    numberOfPlayedSongs = sum(playedSongs)
    percentage = numberOfPlayedSongs * 100 / numberOfSongs

    if counter == 50:
        counter = 0
        printStats(playtime, numberOfPlayedSongs, percentage)

printStats(playtime, numberOfPlayedSongs, percentage)