import socket

ports = []

print("Enter the target IP address.")
ip = input("--> ")

print("Enter the range of ports you want to scan. Ex: 80-85")
port_range = input("--> ").split("-")

for port in range( int(port_range[0]) ,int(port_range[1])+1 ):
    ports.append(port)



for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"\n\n[+] Port {port} is OPEN")
    

    s.close()
print("Port scan completed.")