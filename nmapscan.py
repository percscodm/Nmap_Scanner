import nmap

def scan_with_nmap(target):
    # Create an Nmap Scanner object
    nm = nmap.PortScanner()

    # Perform a basic Nmap scan on the target
    scan_result = nm.scan(hosts=target, arguments='')  # Use '-F' for a fast scan

    # Process and display the scan results
    if target in scan_result['scan']:
        print(f"Scanning {target}...")
        for port in scan_result['scan'][target]['tcp'].keys():
            state = scan_result['scan'][target]['tcp'][port]['state']
            print(f" Port {port} is {state}")

if __name__ == "__main__":
            target_ip = input("Enter the IP address you want to scan: ")  # Enter the IP address or hostname you want to scan
            scan_with_nmap(target_ip)