import requests



# // This script checks only a couple of common misconfigurations and should be expanded upon based on the use case. The Jenkins landscape can be vast with plugins, and each could have its vulnerabilities.
# // Always seek permission before scanning a server or system. Unauthorized scanning can be illegal and unethical.
# // If you find a misconfiguration, notify the system administrator or owner immediately. Never exploit it without explicit permission.



def check_jenkins(target):
    """Check Jenkins misconfigurations."""
    
    # Check if Jenkins is accessible without authentication
    try:
        response = requests.get(f'http://{target}:8080')
        if 'Dashboard [Jenkins]' in response.text:
            print(f"[!] Jenkins dashboard accessible on {target}:8080 without authentication!")
        else:
            print("[+] Jenkins dashboard is not publicly accessible.")
    except requests.ConnectionError:
        print("[+] Jenkins is not running on the default port or the server is down.")

    # Check for scriptConsole access
    try:
        response = requests.get(f'http://{target}:8080/script')
        if 'Jenkins [Jenkins] Script Console' in response.text:
            print(f"[!] Jenkins script console accessible on {target}:8080/script without authentication! High Risk!")
    except requests.ConnectionError:
        print("[+] Jenkins scriptConsole seems to be secured or not running on the default port.")

def main():
    target = input("Enter the target IP or domain: ")
    check_jenkins(target)

if __name__ == "__main__":
    main()
