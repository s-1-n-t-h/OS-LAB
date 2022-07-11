import sys
import os

pid = os.fork()

if pid>0:
    print("In Parent Process: ",os.getpid())
    status = os.wait()
    print("child process ID: ",pid)
    sys.exit("\nExiting Parent Process...\n")
else:
    print("In Child Process: ",os.getpid())
    print("Parent Process ID: ",os.getppid())
    sys.exit('\nExiting Child Process...\n')
