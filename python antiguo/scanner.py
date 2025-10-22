import nmap

scanner = nmap.PortScanner()

ip = input("Ingresa una direccion ip: ")
print(f"Colocaste la ip: {ip}")

scanner.scan(ip)