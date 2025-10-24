import socket

def find_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP address for {domain}: {ip}")
        return ip
    except socket.gaierror:
        print(f"Could not resolve IP for {domain}. Check the domain or your network.")
        return None

if __name__ == "__main__":
    domain = "example.com"  # Target domain
    find_ip(domain)
