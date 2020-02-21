import datetime
import random
import matplotlib.pyplot as plt 

def generateAndPrintStats(playtime, playedSongs, perc, playtimesForGraph, numberOfSongsForGraph):
    print(str(round(playtime)) + ";" + str(playedSongs) + ";" + str(round(perc, 2)))
    playtimesForGraph.append(playtime / 1000)
    numberOfSongsForGraph.append(numberOfPlayedSongs)

numberOfSongs = 8226
playlistLengthInMinutes = 33846
playedSongs = [0] * numberOfSongs

numberOfPlayedSongs = 0
counter = 0
playtime = 0

playtimesForGraph = []
numberOfSongsForGraph = []

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
        generateAndPrintStats(playtime, numberOfPlayedSongs, percentage, playtimesForGraph, numberOfSongsForGraph)

generateAndPrintStats(playtime, numberOfPlayedSongs, percentage, playtimesForGraph, numberOfSongsForGraph)

plt.plot(numberOfSongsForGraph, playtimesForGraph) 
  
plt.xlabel('Anzahl Songs') 
plt.ylabel('Spielzeit in 1000 Minuten')
plt.title('Spielzeit bis alle Songs in Random abgespielt wurden')

plt.show() 