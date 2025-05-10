import requests
import time
import multiprocessing

list_of_resources = ["posts", "comments", "albums", "photos", "users"]
number_of_characters = [0] * len(list_of_resources)

def request_data(i, resource, queue):
    request_url = f"https://jsonplaceholder.typicode.com/{resource}"
    response = requests.get(request_url)
    if response.status_code == 200:
        json_response = response.json()
        string_response = str(json_response)
        len_of_response = len(string_response)
        queue.put(len_of_response)
        print(f"Thread {i}, Downloaded {len_of_response} characters from {request_url}")
    else:
        print(f"Thread {i}, request status code is {response.status_code} for {request_url}")

def manage_processes():
    processes = []
    queues = []
    for i, resource in enumerate(list_of_resources):
        queue = multiprocessing.Queue() 
        process = multiprocessing.Process(target=request_data, args=(i, resource, queue))
        processes.append(process)
        queues.append(queue)
        process.start()

    process_character_count = 0
    for queue in queues:
        process_character_count += queue.get()

    for process in processes:
        process.join()

    print(f"Total number of characters downloaded: {process_character_count}")

if __name__ == "__main__":
    start_time = time.time()
    manage_processes()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
