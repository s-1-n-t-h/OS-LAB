#importing the os module
import os
#creating a child process

pid = os.fork()

if pid>0:
    print("\nThis is the main parent process: ")
    #wait for child process to terminate
    info = os.wait()#os.waitpid(pid,0) #returns a tuple containing pid & exit status of child process
    if os.WIFEXITED(info[1]):
        exit_code = os.WEXITSTATUS(info[1])
        print("Exit code of the child: ",exit_code)

else:
    print("This is child process:")
    print("PID of child process is: ",os.getpid())
    print("Child is now exiting..")
os._exit(os.EX_OK) #terminates the calling process immediately
