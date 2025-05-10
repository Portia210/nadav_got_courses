import os
import multiprocessing


def second_process(name):
    print(f"hello {name}")
    print("this is second process pid: ", os.getpid(), "and the parent pid: ", os.getppid())

def main_process():
    print("this is current process pid: ", os.getpid(), "and the parent pid: ", os.getppid())
    # create a new process
    process = multiprocessing.Process(target=second_process, args=("John",)) # target is the function to run in the new process
    process.start() # start the new process
    process.join() # wait for the new process to finish

if __name__ == "__main__":
    main_process()
