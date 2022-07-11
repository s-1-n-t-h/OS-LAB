from datetime import datetime
#reference string
rString = list(map(int,input("\nReference String: ").split(" ")))
fSize = int(input("\nFrame Size: ")) #frames size of ram

def FIFO(rString,fSize):
    ram = [] #storing frames in ram
    count = 0 #counting page faults
    dict = {}
    for i in range(len(rString)):
        #implementing the algorithm
        if rString[i] in ram:
            continue
        elif len(ram) < fSize:
            dict[rString[i]] = datetime.now()
            ram.append(rString[i])
            count += 1
        else:
            firstIn = sorted(dict.items(), key=lambda x: x[1])
            for j in firstIn:
                pg_no = j[0]
                if pg_no in ram:
                    index = ram.index(pg_no)
                    ram.pop(index)
                    dict[rString[i]] = datetime.now()
                    ram.insert(index,rString[i])
                    count += 1
                    break
    return count


    
print("\nPage Faults using FIFO: ",FIFO(rString,fSize))
        


