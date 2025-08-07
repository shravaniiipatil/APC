print("Configuration system for a web server")

server_ip = ("192.168.1.1",)


allowed_ip = ["192.168.1.10", "192.168.1.20"]

print("Original Configuration:")
print("Server IP:", server_ip[0])
print("Allowed IPs:", allowed_ip)

allowed_ip.append("192.168.1.30")
allowed_ip.remove("192.168.1.10")

print("\nUpdated Configuration:")
print("Server IP:", server_ip[0])
print("Allowed IPs:", allowed_ip)
