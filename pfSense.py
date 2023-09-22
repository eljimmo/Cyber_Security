import requests
from requests.auth import HTTPBasicAuth




#  basic security checks for pfSense firewall/router computer software:

# Default Credentials: Ensure that default credentials like admin:pfsense are not in use.
# Exposed Web Interface: The web configuration interface shouldn't be exposed to the world.
# Weak SSL/TLS Configuration: For the web interface, weak ciphers or protocols should be avoided.
# Unnecessary Services: Ensure services that aren't needed aren't running or exposed.
# Check Firewall Rules: Make sure that there are no overly permissive rules, such as allowing all incoming traffic.
# Outdated Software: Ensure pfSense and its packages are updated regularly.

def check_pfsense_config(target):
    """Check pfSense for common misconfigurations."""
    
    # Check if the web interface is accessible
    try:
        response = requests.get(f'http://{target}', timeout=5)
        if 'pfSense' in response.text:
            print(f"[!] pfSense web interface is accessible at {target}.")

            # Check for default credentials
            response = requests.get(f'http://{target}', 
                                    auth=HTTPBasicAuth('admin', 'pfsense'), 
                                    timeout=5)
            if 'Dashboard' in response.text:
                print(f"[!!] Default credentials (admin:pfsense) are in use!")
            else:
                print("[+] Default credentials are not in use.")
        else:
            print("[+] pfSense web interface is not publicly accessible or is not running on the default port.")
    
    except requests.ConnectionError:
        print("[+] pfSense web interface seems to be secured or not running on the default port.")
    except requests.Timeout:
        print("[!] The request to the pfSense interface timed out. It may be heavily filtered or facing network issues.")

def main():
    target = input("Enter the target IP or domain (without http://): ")
    check_pfsense_config(target)

if __name__ == "__main__":
    main()
