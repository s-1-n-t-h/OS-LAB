import os

pid = os.fork()

if pid:
    #wait for the child process to get exected 
    status = os.wait() # returna a tuple containg child process ID and 
    # exit status indication
    print('\nIn parent Process-')
    print("Terminated child's process id: ",status[0])
    print("Signal number that killed the child process: ",status[1])
else:
    print("In Child Process-")
    print("Process ID: ",os.getpid())
    print("Exiting")
