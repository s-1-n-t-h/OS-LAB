n = int(input("Number of process: "))

pid = []
allocated = [[] for i in range(n)]
max_need = [[] for i in range(n)]
available = []
remaining_need = [[] for i in range(n)]
total_resources = []
dead_lock_avoidance_pattern = []
completed_index = []
# taking process ID's
pid.extend(list(input("Process ID's: ").split(" ")))
print("Given Process ID's:", pid)

# taking allocated resources count of each type to each process
for i in range(n):
    allocated[i].extend(
        list(map(int, input("Allocated Resources for "+pid[i]+": ").split(" "))))
print("Resource allocated for each process: ", allocated)

# taking need of each type of resource to each process
for i in range(n):
    max_need[i].extend(
        list(map(int, input("Max Need of Resources for "+pid[i]+": ").split(" "))))
print("Maximum need of resources for each process: ", max_need)

# taking total resources available for each type
total_resources.extend(list(map(int, input("Total Resources: ").split(" "))))
print("Total Resources entered: ", total_resources)
allocated_sum = [0 for i in range(len(allocated[0]))]

# adding total resources of each type allocated to each process
for process in allocated:
    for j in range(len(process)):
        allocated_sum[j] += process[j]

# finding available resources
for i in range(len(total_resources)):
    available.append(total_resources[i]-allocated_sum[i])
print("Sum of each type of resources: ", allocated_sum)
print("Total Resources available after allocation: ", available)

# calculating remaining need for each process
for i in range(len(remaining_need)):
    for j in range(len(max_need[i])):
        remaining_need[i].append(max_need[i][j] - allocated[i][j])
print("Remaining Need: ", remaining_need)
while(len(dead_lock_avoidance_pattern)!=n):

    for i in range(len(remaining_need)):
        if(available >= remaining_need[i]):
            if i in completed_index:
                continue
            dead_lock_avoidance_pattern.append(pid[i])
            completed_index.append(i)
            available = [available[j] + allocated[i][j] for j in range(len(available))]

print("The pattern of Process to avoid Dead lock according to Banker's algirthm is: ",dead_lock_avoidance_pattern)

