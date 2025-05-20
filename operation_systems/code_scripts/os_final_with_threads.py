import requests
import time
import threading

list_of_resources = ["posts", "comments", "albums", "photos", "users"]
number_of_characters = [0] * len(list_of_resources)

def request_data(i, resource):
    request_url = f"https://jsonplaceholder.typicode.com/{resource}"
    response = requests.get(request_url)
    if response.status_code == 200:
        json_response = response.json()
        string_response = str(json_response)
        len_of_response = len(string_response)
        number_of_characters[i] = len_of_response
        print(f"Thread {i}, Downloaded {len_of_response} characters from {request_url}")
    else:
        print(f"Thread {i}, request status code is {response.status_code} for {request_url}")

def manage_threads():
    threads = []
    for i, resource in enumerate(list_of_resources):
        thread = threading.Thread(target=request_data, args=(i, resource))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    manage_threads()
    end_time = time.time()
    print(f"Total number of characters downloaded: {sum(number_of_characters)}")
    print(f"Total time taken: {end_time - start_time} seconds")
