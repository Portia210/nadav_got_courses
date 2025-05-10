import requests
import time
from multiprocessing import Pool

list_of_resources = ["posts", "comments", "albums", "photos", "users"]

def fetch_data(resource):
    start_time = time.time()
    requests.get(f"https://jsonplaceholder.typicode.com/{resource}")
    end_time = time.time()  
    return end_time - start_time

if __name__ == "__main__":
    start_time = time.time()
    
    # Create a pool of workers
    with Pool(processes=len(list_of_resources)) as pool:
        # Start all requests in parallel
        start_iter_time = time.time()
        results = pool.map(fetch_data, list_of_resources)
        end_iter_time = time.time()
        
        # Print results
        total_request_time = sum(results)
        iter_duration = end_iter_time - start_iter_time
        
        print(f"Total iteration time: {iter_duration:.3f} seconds")
        print(f"Average request time: {total_request_time/len(results):.3f} seconds")
        print(f"Overhead per request: {(iter_duration - total_request_time)/len(results):.3f} seconds")
        
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.3f} seconds")