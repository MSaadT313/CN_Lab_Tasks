import socket 

hostname = input("Enter hostname: ").strip()

try:
    ip_address = socket.gethostbyname(hostname)
    print(f"IP address of {hostname}: {ip_address}")
except Exception:
    print(f"Hostname {hostname} cannot be resolved")


try:
    port = int(input("Enter Port Number: "))
    protocol = input("Enter Protocol: ").strip().lower()

    if not 0 <= port <= 65535:
        print("Invalid port number")
    else:
        try:
            service = socket.getservbyport(port, protocol)
            print("Service Name: ",service)
        except Exception:
            print("Unknown Service")
except Exception:
    print("Invalid Port Number")

