import socket

def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout for each connection attempt

        try:
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
        except socket.error:
            print(f"Couldn't connect to {target_ip}.")
            break
        finally:
            sock.close()

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f" - Port {port}")
    else:
        print("No open ports found in the specified range.")

def main():
    try:
        target_ip = input("Enter target IP address: ").strip()
        socket.inet_aton(target_ip)  # Validate IP address

        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Port numbers must be between 0 and 65535.")
            return

        scan_ports(target_ip, start_port, end_port)

    except ValueError:
        print("Please enter valid numbers for ports.")
    except socket.error:
        print("Invalid IP address.")

if __name__ == "__main__":
    main()
