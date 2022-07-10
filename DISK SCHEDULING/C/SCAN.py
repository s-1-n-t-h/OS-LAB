from audioop import reverse
import re


reqSeq = list(map(int, input("Request String: ").split(" ")))
position = int(input("Initial head position: "))
dir = int(input("Direction 1:right 0:left : "))

def SSTF(reqSeq,initPos,dir):
    seek_time = 0
    seekSeq = [initPos]
    if dir == 1:
        # left to right ascending
        reqSeq.sort()
        reqSeq.insert(0,0) # end of disk to left is 0 and right is max of request
    else:
        # right to left descending
        reqSeq.sort(reverse=True)
        # end of disk to left is max of request and right is 0
        reqSeq.append(0)
    while reqSeq:
        seek_time += abs(initPos-reqSeq[0]) # calculating seek time
        initPos = reqSeq[0] # updating initial position
        seekSeq.append(reqSeq.pop(0)) # removing served requests
    return (seek_time,seekSeq)

tup = SSTF(reqSeq,position,dir)
print("FCFS Seek Time: ",tup[0])
print("Seek Sequence: ",tup[1])