n = int(input('\nNo of Process: '))
pcb_queue = []
executed_process_queue = []
TWT = 0;#total waiting time
TTAT = 0#total turn around time
for i in range(n):
    print("\nEnter:\n")
    # [PID, BT, [ALCT, TT]]
    pcb_queue.append([input("Process ID: "),int(input("Burst Time: ")),[]])
    
time_elapsed = 0
time_qunata = int(input("\nTime Quanta: "))
no_of_programs_left = len(pcb_queue) #calculating no of programs in schedule
# for running the schedule until all the process in schedule are executed
while(no_of_programs_left!=0):
    #for each process left in the queue
    process = pcb_queue[0]
                                
    process[2].append(time_elapsed) # appending time of allocation of CPU to the process
    if process[1] <= time_qunata:
        time_elapsed += process[1] 
        process[1] = 0 #process is completely executed
    else:
        time_elapsed += time_qunata
        process[1] -= time_qunata #updating remaining burst time

    process[2].append(time_elapsed) # appending termination time 
    #to decide whether to remove from queue or to re append to queue
    if process[1]==0:
        executed_process_queue.append(pcb_queue.pop(0))
    else:
        pcb_queue.append(pcb_queue.pop(0))
    
    no_of_programs_left = len(pcb_queue)
        
print("\npcb: ",pcb_queue)
print('\ngantt chart: ',executed_process_queue)
print("\nTotal Turn Around Time of the Schedule: ",(executed_process_queue[-1][-1][-1]-0))#last process termination time - arrival time of first process (0) here


#for calculating multiple waiting times
for process in executed_process_queue:
    # waiting time in preemption is wt = new allocation time [-2] - old termination time [-3] or //termination time - burst time//-not used 
    TWT += ( sum(process[2][0::2]) - sum(process[2][1:-1:2]))

print('\nTotal Waiting Time: ',TWT)
print("\nAverage Waiting Time: ",end="") # cpu alloted time - arrival time [3] - [1]
AWT = TWT/n # calculating average waiting time
print(round(AWT,3)) #avg waiting time


for process in executed_process_queue:
    TTAT+= process[-1][-1]-0    

print("\nTotal Turn Around Time: ",TTAT)
print("\nAverage Turn Around Time: ",end="") # termination time - arrival time [4] - [1]
ATAT = TTAT/n # calculating average turn around time
print(round(ATAT,3),'\n')
