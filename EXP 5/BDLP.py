
def CircularWait():
    pid = input("Process ID:")
    res = list(input('Resources in system: ').split(" "))
    res.sort()
    mark_allocation = []
    print("Resources Available: ", res)
    while(True):
        resNeeded = input("Resource Needed: ")
        if resNeeded in res:
            try:
                if (resNeeded not in mark_allocation) and (resNeeded > mark_allocation[-1]):
                    print("Resource "+resNeeded+" is allocated")
                    mark_allocation.append(resNeeded)
                else:
                    print("Request for Resouces with lower Priority can't be granted!")
            except:
                if (resNeeded not in mark_allocation):
                    print("Resource "+resNeeded+" is allocated")
                    mark_allocation.append(resNeeded)
                else:
                    print("Request for Resouces with lower Priority can't be granted!")

        else:
            print("Invalid Resource")
            break


CircularWait()