n = int(input('\nNo of Process: '))
pcb_queue = []
TWT = 0; TTAT = 0
for i in range(n):
    print("\nEnter:\n")
    pcb_queue.append([input("Process ID: "),int(input("Arrival Time:")),int(input("Burst Time: "))])
    
time_elapsed = 0
#no sorting is required as FCFS
for process in pcb_queue:
    process.append(time_elapsed)
    time_elapsed += process[2]
    process.append(time_elapsed)
    
print("\nTotal Turn Around Time of the Schedule: ",(pcb_queue[-1][-1]-pcb_queue[0][3])) #last process termination time - arrival time of first process

print("\nAverage Waiting Time: ",end="") # cpu alloted time - arrival time [3] - [1]

for process in pcb_queue:
    TWT += process[3]-process[1]
    
AWT = TWT/n

print(round(AWT,3))

print("\nAverage Turn Around Time: ",end="") # termination time - arrival time [4] - [1]

for process in pcb_queue:
    TTAT+= process[4]-process[1]
    
ATAT = TTAT/n

print(round(ATAT,3),'\n')
