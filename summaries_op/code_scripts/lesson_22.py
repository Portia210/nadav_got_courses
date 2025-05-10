import threading
import time
import random
x = 0


number_of_threads = 5
lock_counters = [0] * number_of_threads # expected output: [0, 0, 0]
# the reason why we createing this, so that each thread will have its own counter
# if we don't do this, all the threads will be using the same counter, and the result will be incorrect

# method 1: using lock
def task_lock(i, mutex):
    for _ in range(100):
        mutex.acquire()
        temp = lock_counters[i]
        temp += 1
        time.sleep(0.00001*random.randint(1, 3)) # in the sleep time the os will do context switch
        lock_counters[i] = temp
        mutex.release()
    print(f"task lock counter: {lock_counters}")


def manage_threads_with_lock():
    mutex = threading.Lock()
    threads = []
    for i in range(number_of_threads):
        thread = threading.Thread(target=task_lock, args=(i, mutex))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    print(f"count sum: {sum(lock_counters)}")


# method 2: using semaphore basic
def task_semaphore(semaphore):
    global x
    for i in range(100):
        semaphore.acquire()
        temp = x
        temp += 1
        
        time.sleep(0.00001*random.randint(1, 3))
        x = temp
        semaphore.release()
    print(f"x: {x}")

def manage_threads_with_semaphore():
    semaphore = threading.Semaphore(1)
    threads = []
    for i in range(3):
        thread = threading.Thread(target=task_semaphore, args=(semaphore,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    manage_threads_with_lock()
    manage_threads_with_semaphore()
