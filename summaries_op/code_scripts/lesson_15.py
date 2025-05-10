import requests
import multiprocessing
import time
list_of_resources = ["posts", "comments", "albums", "photos", "users"]

def fetch_data(resource, queue):
    start_time = time.time()
    requests.get(f"https://jsonplaceholder.typicode.com/{resource}")
    end_time = time.time()  
    queue.put((resource, end_time - start_time))


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    start_time = time.time()
    processes = []
    
    # Start all processes first without waiting
    start_iter_time = time.time()
    for resource in list_of_resources:
        process = multiprocessing.Process(target=fetch_data, args=(resource, queue))
        process.start()
        processes.append(process)
    
    # Now collect all results
    results = []
    for _ in range(len(list_of_resources)):
        resource, response_time = queue.get()
        results.append((resource, response_time))
    
    end_iter_time = time.time()
    total_duration = end_iter_time - start_iter_time
    
    # Print results
    for resource, response_time in results:
        print(f"Resource: {resource}")
        print("response time: ", response_time)
        print("--------------------------------")

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("total iterations duration: ", total_duration)
    end_time = time.time()
    print(f"time taken: {end_time - start_time} seconds")


