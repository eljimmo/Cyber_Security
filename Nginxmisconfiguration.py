import requests


# // This script provides basic checks, and many other potential misconfigurations or vulnerabilities might exist based on the individual use-case of Nginx.
# // Always seek permission before scanning a server or system. Unauthorized scanning can be illegal and unethical.
# // If you find a misconfiguration, notify the system administrator or owner immediately. Never exploit it without explicit permission.



def check_nginx_config(target):
    """Check Nginx misconfigurations."""
    
    # Check for Information Disclosure
    try:
        response = requests.get(f'http://{target}')
        server_header = response.headers.get('Server', '')
        if 'nginx' in server_header:
            print(f"[!] Nginx server version disclosed: {server_header}")
        else:
            print("[+] Nginx server version is not disclosed.")
    except requests.ConnectionError:
        print("[!] Couldn't connect to the server.")

    # Check for Directory Listing
    common_dirs = ["/uploads", "/images", "/img", "/assets"]
    for dir in common_dirs:
        response = requests.get(f'http://{target}{dir}')
        if '<title>Index of' in response.text:
            print(f"[!] Directory listing enabled for {dir}")
    
    # Check for exposed .git directory
    response = requests.get(f'http://{target}/.git/HEAD')
    if 'ref: refs/heads' in response.text:
        print(f"[!] Exposed .git directory detected!")

    # Check for Security Headers
    security_headers = [
        ('X-Frame-Options', 'Mitigates clickjacking attacks.'),
        ('X-Content-Type-Options', 'Prevents MIME-type sniffing.'),
        ('Strict-Transport-Security', 'HTTP Strict Transport Security (HSTS).')
        # Add other headers as needed
    ]
    
    for header, description in security_headers:
        if header not in response.headers:
            print(f"[!] Missing {header}. {description}")
        else:
            print(f"[+] {header} is present.")

def main():
    target = input("Enter the target IP or domain (without http://): ")
    check_nginx_config(target)

if __name__ == "__main__":
    main()
