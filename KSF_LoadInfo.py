import json
from collections import defaultdict

# Loads Dicts (maps) from Json Files
with open('beginnerMapTime.json', 'r') as f:
    t1MapTime = json.load(f)
with open('regularMapTime.json', 'r') as f:
    regMapTime = json.load(f)

# Counts total time of maps played and moves dict into 2D list
t1TotalTime = 0
t1MapsList = []
for mapName, mapTime in t1MapTime.items():
    t1TotalTime += mapTime
    t1MapsList.append([mapName, mapTime])
# Sorts list by playtime in descending order
t1MapsList.sort(key = lambda x: x[1], reverse = True)

# Counts total time of maps played and moves dict into 2D list
regTotalTime = 0
regMapList = []
for mapName, mapTime in regMapTime.items():
    regTotalTime += mapTime
    regMapList.append([mapName, mapTime])
# Sorts list by playtime in descending order
regMapList.sort(key = lambda x : x[1], reverse = True)




