#reference string
rString = list(map(int,input("\nReference String: ").split(" ")))
fSize = int(input("\nFrame Size: ")) #frames size of ram

def FIFO(rString,fSize):
    ram = [] #storing frames in ram
    count = 0 #counting page faults
    for i in range(len(rString)):
        #implementing the algorithm
        if rString[i] in ram:
            continue
        elif len(ram) < fSize:
            ram.append(rString[i])
            count += 1
        else:
            ram.pop(0)
            ram.insert(0,rString[i])
            count += 1
    return count

print("\nFIFO: ",FIFO(rString,fSize))
        


