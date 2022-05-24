n = int(input('\nNo of Process: '))
pcb_queue = []
TWT = 0;#total waiting time
TTAT = 0#total turn around time
for i in range(n):
    print("\nEnter:\n")
    pcb_queue.append([input("Process ID: "),int(input("Burst Time: ")),int(input("Priority: "))])
    
def key_returner(l):
    return l[2]
pcb_queue.sort(key=key_returner)

time_elapsed = 0

for process in pcb_queue:
    process.append(time_elapsed)
    time_elapsed += process[1]
    process.append(time_elapsed)

print('\ngantt chart: ',pcb_queue)
    
print("\nTotal Turn Around Time of the Schedule: ",(pcb_queue[-1][-1]-0)) #last process termination time - arrival time of first process



for process in pcb_queue:
    TWT += process[4]-process[1] # tat - bt

print('\nTotal Waiting Time: ',TWT)
print("\nAverage Waiting Time: ",end="") # cpu alloted time - arrival time [3] - [1]
AWT = TWT/n

print(round(AWT,3))

for process in pcb_queue:
    TTAT+= process[4]#-0

print("\nTotal Turn Around Time: ",TTAT)
print("\nAverage Turn Around Time: ",end="") # termination time - arrival time [4] - [1]

ATAT = TTAT/n

print(round(ATAT,3),'\n')
