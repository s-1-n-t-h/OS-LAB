n = int(input('\nNo of Process: '))
pcb_queue = []
executed_process_queue = []
TWT = 0  # total waiting time
TTAT = 0  # total turn around time
for i in range(n): 
    print("\nEnter:\n")  #[pid, bt, alt, tt]
    pcb_queue.append([input("Process ID: "), int(input("Burst Time: ")),[]])

def key_returner(l):
    return l[1]


pcb_queue.sort(key=key_returner)

time_elapsed = 0

no_of_programs_left = len(pcb_queue)  # calculating no of programs in schedule
# for running the schedule until all the process in schedule are executed
while(no_of_programs_left != 0):
    #for each process left in the queue
    process = pcb_queue[0]

    process[2].append(time_elapsed)
    if process[1] == 0:
       executed_process_queue.append(pcb_queue.pop(0))
    else:
        process[2].append(time_elapsed)
        time_elapsed += 1
        process[1] -= 1
        process[2].append(time_elapsed)
    pcb_queue.sort(key=key_returner)
    no_of_programs_left = len(pcb_queue)
    

# last process termination time - arrival time of first process
print("\nTotal Turn Around Time of the Schedule: ",(executed_process_queue[-1][-1][-1]-executed_process_queue[0][2][0]))
print(executed_process_queue)
##for calculating multiple waiting times
for process in executed_process_queue:
    # waiting time in preemption is wt = new allocation time [-2] - old termination time [-3] or //termination time - burst time//-not used
    TWT += (sum(process[2][0::2]) - sum(process[2][1:-1:2]))

# cpu alloted time - arrival time [3] - [1]
print("\nAverage Waiting Time: ", end="")

AWT = TWT/n

print(round(AWT, 3))

# termination time - arrival time [4] - [1]
print("\nAverage Turn Around Time: ",end="") # termination time - arrival time [4] - [1]

for process in executed_process_queue:
    TTAT+= process[-1][-1]#-0
    
ATAT = TTAT/n

print(round(ATAT,3),'\n')