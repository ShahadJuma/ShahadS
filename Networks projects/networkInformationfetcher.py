import socket
import requests

def get_network_info():
    """
    Fetches and displays basic network information including hostname and public IP.
    """
    try:
        # Get the hostname
        hostname = socket.gethostname()
        
        # Get the local IP address
        local_ip = socket.gethostbyname(hostname)
        
        # Get the public IP address
        public_ip = requests.get('https://api.ipify.org').text
        
        return {
            "Hostname": hostname,
            "Local IP": local_ip,
            "Public IP": public_ip
        }
    except Exception as e:
        return {"Error": str(e)}

# Example usage:
network_info = get_network_info()
for key, value in network_info.items():
    print(f"{key}: {value}")
