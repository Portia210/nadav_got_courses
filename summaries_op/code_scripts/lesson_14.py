import os
import multiprocessing
import time


def second_process(name, queue):
    print(f"hello {name}")
    print("this is second process pid: ", os.getpid(), "and the parent pid: ", os.getppid())
    time.sleep(2)
    queue.put("Hello from second process")

def main_process():
    queue = multiprocessing.Queue()
    print("this is current process pid: ", os.getpid(), "and the parent pid: ", os.getppid())
    # create a new process
    process = multiprocessing.Process(target=second_process, args=("Johhny", queue)) # target is the function to run in the new process
    process.start() # start the new process
    time.sleep(2)
    process.join() # wait for the new process to finish
    print(queue.get())

if __name__ == "__main__":
    start_time = time.time()
    main_process()
    end_time = time.time()
    print(f"time taken: {end_time - start_time} seconds")
