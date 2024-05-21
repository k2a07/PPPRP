import requests
import time

def stats_to_file():
    try:
        resp = requests.get('http://my-service/statistics')
        t_request_cnt = resp.json()['t_request_cnt']

        with open('stats.txt', 'a') as file:
            file.write(f'{t_request_cnt}\n')

    except Exception as exception:
        print(f'An error appeared: {exception}')

while True:
    stats_to_file()
    time.sleep(5)