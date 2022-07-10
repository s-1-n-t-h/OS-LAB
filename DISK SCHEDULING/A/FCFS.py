reqSeq = list(map(int,input("Request String: ").split(" ")))
position = int(input("Initial head position: "))

def FCFS(reqSeq,initPos):
    seek_time = 0
    seekSeq = [initPos]  # initial position
    for i in reqSeq:
        seek_time += abs(i - initPos)  # adding seek time
        initPos = i  # updating initial position
    return (seek_time,seekSeq)

tup = FCFS(reqSeq,position)
print("FCFS Seek Time: ",tup[0])
print("Seek Sequence: ",tup[1])