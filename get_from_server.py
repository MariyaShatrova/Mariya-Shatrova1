import requests
import time

last_time = 0

while True:
    response = requests.get('http://127.0.0.1:5000/get_messages')

    for message in response.json()['messages']:
        if message['timestamp'] > last_time:
        print(message)
    last_time = time.time
