#module used for intercating with operating system

import os

#creating a child process

pid = os.fork()

if pid > 0:
    print("I'm parent process:" )
    print('Process ID: ',os.getpid()) # gives pid of current process
    print("Child's process ID: ",pid)

else:
    print('\nI am child process:')
    print("process ID: ",os.getpid())
    print("Parent's process ID: ",os.getppid())
