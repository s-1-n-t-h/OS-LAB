#reference string
from datetime import datetime
rString = list(map(int, input("\nReference String: ").split(" ")))
fSize = int(input("\nFrame Size: "))  # frames size of ram


def LRU(rString, fSize):
    ram = []  # storing frames in ram
    count = 0  # counting page faults
    dict = {} # dictionary to maintain time stamps of pages into ram
    for i in range(len(rString)):
        #implementing the algorithm
        if rString[i] in ram: # if page is already in ram
            dict[rString[i]] = datetime.now() #updating the timestamp of the page as it is used
            continue
        elif len(ram) < fSize: #if the ram is not full
            dict[rString[i]] = datetime.now()
            ram.append(rString[i])
            count += 1
        else: #if the ram is full - replae the page that is least recently used in ram
            leastUsed = sorted(dict.items(), key=lambda x: x[1])
            for j in leastUsed:
                pg_no = j[0]
                if pg_no in ram:
                    ram.remove(pg_no)
                    dict[rString[i]] = datetime.now()
                    ram.append(rString[i])
                    count += 1
                    break
                
    return count
        
print("\nLRU: ", LRU(rString, fSize))
