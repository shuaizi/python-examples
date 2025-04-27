import socket

def get_domain_from_ip(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return None

# Example usage
if __name__ == "__main__":
    ip = "8.8.8.8"  # Replace with the IP address you want to query
    domain = get_domain_from_ip(ip)
    if domain:
        print(f"The domain name for IP {ip} is {domain}.")
    else:
        print(f"No domain name found for IP {ip}.")
