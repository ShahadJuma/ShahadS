
# Establish SSH connection
net_connect = ConnectHandler(**device)

# Enter enable mode
net_connect.enable()

# Send configuration commands
config_commands = [
    'interface GigabitEthernet0/1',
    'description Automated Configuration via Python',
    'ip address 192.168.1.2 255.255.255.0',
    'no shutdown',
]
output = net_connect.send_config_set(config_commands)

# Display the output
print(output)

# Disconnect the session
net_connect.disconnect()