# no of processes
n = int(input("Number of Process: "))
# pcb block for each process
pcb_queue = []
# setting
twt, ttat, time_elapsed = 0, 0, 0

for i in range(n):
    print("Enter:\n")
    pcb_queue.append([input("Process ID: "), int(
        input("Arrival Time: ")), int(input("Burst Time: "))])

pcb_queue.sort(key=lambda x: x[1])

for process in pcb_queue:
    if process[0] == pcb_queue[0][0]:
        # if it is the first process, start time for schedule is it's arrival time
        time_elapsed += process[1]
    # updating waiting time of process   - time of cpu allocation - arrival time
    twt += time_elapsed - process[1]
    time_elapsed += process[2]  # updating time elapsed with adding burst time
    # completion time - time of submission into queue (arrival time)
    ttat = time_elapsed - process[1]

print("Average Waiting Time: {} ms".format(twt/n))
print("Average Turn Around Time: {} ms".format(ttat/n))
print("Total Turn Around Time: {} ms".format(time_elapsed-pcb_queue[0][1]))
