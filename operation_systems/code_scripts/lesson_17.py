import threading
import time
import random
import requests

# basic threading
def number_printer(num):
    print(f"worker {num} started")
    time.sleep(random.randint(1, 3))
    print(f"worker {num} finished") # thread will not finish in the order of the loop, it will finish when the thread is done

def threads_manager():
    threads = []
    for i in range(8):
        thread = threading.Thread(target=number_printer, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()



# how to return data with threads
list_of_resources = ["posts", "comments", "albums", "photos", "users"]

def fetch_data(resource, returns):
    start_time = time.time()
    requests.get(f"https://jsonplaceholder.typicode.com/{resource}")
    end_time = time.time()  
    returns.append(end_time - start_time)

def manage_data_threads():
    data_threads = []
    returns = []
    for resource in list_of_resources:
        thread = threading.Thread(target=fetch_data, args=(resource, returns))
        data_threads.append(thread)
        thread.start()
    for thread in data_threads:
        thread.join()
    print(max(returns))

manage_data_threads()


