import os
import multiprocessing
import time


def second_process(name):
    print(f"hello {name}")
    print("this is second process pid: ", os.getpid(), "and the parent pid: ", os.getppid())
    time.sleep(2)

def main_process():
    print("this is current process pid: ", os.getpid(), "and the parent pid: ", os.getppid())
    # create a new process
    process = multiprocessing.Process(target=second_process, args=("John",)) # target is the function to run in the new process
    process.start() # start the new process
    time.sleep(2)
    process.join() # wait for the new process to finish

if __name__ == "__main__":
    start_time = time.time()
    main_process()
    end_time = time.time()
    print(f"time taken: {end_time - start_time} seconds")
