import a2s
import threading
import json
from collections import defaultdict

t1MapTime = defaultdict(int)
regMapTime = defaultdict(int)
def checkServers():
    # Beginner Servers tierLocationValue
    t1uscAddy = ("74.91.115.159", 27015) 
    t1uscInfo = a2s.info(t1uscAddy)
    t1MapTime[t1uscInfo.map_name]+=1
    t1useAddy = ("74.91.123.51", 27030)
    t1useInfo = a2s.info(t1useAddy)
    t1MapTime[t1useInfo.map_name]+=1
    t1euAddy = ("185.107.96.64", 27019)
    t1euInfo = a2s.info(t1euAddy)
    t1MapTime[t1euInfo.map_name]+=1
    # Regular Servers tierLocationValue
    regUsAddy = ("74.91.123.51", 27015)
    regUsInfo = a2s.info(regUsAddy)
    regMapTime[regUsInfo.map_name]+=1
    regEuAddy = ("185.107.96.64", 27016)
    regEuInfo = a2s.info(regEuAddy)
    regMapTime[regEuInfo.map_name]+=1
    regAuAddy = ("139.99.149.210", 27015)
    regAuInfo = a2s.info(regAuAddy)
    regMapTime[regAuInfo.map_name]+=1
    threading.Timer(300, checkServers).start()
def writeInfo():
    with open('beginnerMapTime.json', 'w') as f:
        json.dump(t1MapTime, f)
    with open('regularMapTime.json', 'w') as f:
        json.dump(regMapTime, f)
    threading.Timer(3600*6, writeInfo).start()
checkServers()
writeInfo()


    


