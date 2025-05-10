import threading
import time
x = 0

def task():
    global x
    for i in range(100):
        temp = x
        temp += 1
        time.sleep(0.00001) # in the sleep time the os will do context switch
        x = temp

    print(f"x: {x}")


def main():
    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
    
