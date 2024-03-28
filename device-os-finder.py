import nmap

def os_detection_scan(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-O')  # -O enables OS detection

    for host in nm.all_hosts():
        if 'osclass' in nm[host]:
            for osclass in nm[host]['osclass']:
                print(f"IP Address: {host}")
                print(f"OS Name: {osclass['osfamily']} {osclass['osgen']}")
                print(f"Accuracy: {osclass['accuracy']}%")
                print(f"Vendor: {osclass['vendor']}")
                print("")

if __name__ == "__main__":
    network_range = '192.168.1.0/24'  # Replace with your network range
    os_detection_scan(network_range)