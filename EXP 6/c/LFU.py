from collections import Counter
from datetime import datetime
# reference string
rString = list(map(int, input("\nReference String: ").split(" ")))
fSize = int(input("\nFrame Size: "))  # frames size of ram


def LFU(rString, fSize):
    ram = []  # storing frames in ram
    count = 0  # counting page faults
    dict = {} # dictionary to maintain time stamps of pages into ram
    for i in range(len(rString)):
        # implementing the algorithm
        if rString[i] in ram:
            dict[rString[i]] = datetime.now()
            continue
        elif len(ram) < fSize:
            dict[rString[i]] = datetime.now()
            ram.append(rString[i])
            count += 1
        else:
            freq = Counter(rString[:i])

            leastFreq = sorted(freq.items(),key=lambda x:x[1])
            for j in leastFreq:
                sameFreq = [m[0] for m in leastFreq if m[1] == j[1]]
                diffByTs = sorted([[k,dict[k]] for k in sameFreq],key=lambda x:x[1])
                flag = 0
                for k in diffByTs:
                    pg_no = k[0]
                    if (pg_no in ram):
                        flag = 1
                        index = ram.index(pg_no)
                        ram.pop(index)
                        dict[rString[i]] = datetime.now()
                        ram.insert(index,rString[i])
                        count += 1
                        break
                if flag == 1:
                    break
    return count

print("\nPage Faults using LFU: ", LFU(rString, fSize))
