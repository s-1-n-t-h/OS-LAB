reqSeq = list(map(int, input("Request String: ").split(" ")))
position = int(input("Initial head position: "))

def SSTF(reqSeq,initPos):
    seek_time = 0
    seekSeq = [initPos] # initial position
    while reqSeq:
        calSeekTime = [abs(initPos-i) for i in reqSeq]  # calculating seek time
        shortest = min(calSeekTime) # finding shortest seek time
        index = calSeekTime.index(shortest) # mapping shortest distance to it's respective disk position in request sequence
        initPos = reqSeq[index]  # updating initial position
        seek_time += shortest # adding seek time
        seekSeq.append(reqSeq.pop(index))  # removing served requests
    return (seek_time,seekSeq)

tup = SSTF(reqSeq,position)
print("FCFS Seek Time: ",tup[0])
print("Seek Sequence: ",tup[1])