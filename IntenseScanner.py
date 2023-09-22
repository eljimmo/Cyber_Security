import os
import subprocess


# //Ensure all tools (nmap, gobuster, nikto, masscan, portSpider) are installed and accessible from the command line.
# //Ensure all tools (nmap, gobuster, nikto, masscan, portSpider) are installed and accessible from the command line.

# //masscan can be extremely aggressive, hence the rate limit (--rate=1000). Adjust this rate based on your needs and the capabilities of your network.
# //masscan can be extremely aggressive, hence the rate limit (--rate=1000). Adjust this rate based on your needs and the capabilities of your network.


# // Always run scans only against targets you have explicit permission to scan. Unauthorized scanning is both illegal and unethical. 
# // Always run scans only against targets you have explicit permission to scan. Unauthorized scanning is both illegal and unethical.

def run_nmap(target):
    """Run nmap scan on the target."""
    print(f"[+] Starting nmap scan on {target}")
    command = ["nmap", "-A", "-T4", "-oA", "nmap_output", target]
    subprocess.run(command)
    print(f"[+] Nmap scan completed for {target}")

def run_gobuster(target):
    """Run gobuster scan on the target."""
    print(f"[+] Starting gobuster scan on {target}")
    wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
    extensions = "php,html,js,txt"
    command = ["gobuster", "dir", "-u", f"http://{target}", "-w", wordlist, "-x", extensions, "-o", "gobuster_output.txt"]
    subprocess.run(command)
    print(f"[+] Gobuster scan completed for {target}")

def run_nikto(target):
    """Run nikto scan on the target."""
    print(f"[+] Starting nikto scan on {target}")
    command = ["nikto", "-h", target, "-o", "nikto_output.txt"]
    subprocess.run(command)
    print(f"[+] Nikto scan completed for {target}")

def run_masscan(target):
    """Run masscan on the target."""
    print(f"[+] Starting masscan on {target}")
    command = ["masscan", "-p1-65535", target, "--rate=1000", "-oL", "masscan_output.txt"]
    subprocess.run(command)
    print(f"[+] Masscan completed for {target}")

def run_portSpider(target):
    """Run portSpider on the target."""
    print(f"[+] Starting portSpider scan on {target}")
    command = ["portSpider.py", target]  # Assuming portSpider is invoked this way, adjust if different
    subprocess.run(command)
    print(f"[+] portSpider scan completed for {target}")

def main():
    target = input("Enter the target IP: ")
    consent = input(f"Are you sure you want to scan {target}? (yes/no): ").lower()
    if consent != 'yes':
        print("Scan aborted!")
        return

    run_masscan(target)  # Running masscan first as it's fast and can provide an overview
    run_nmap(target)
    run_gobuster(target)
    run_nikto(target)
    run_portSpider(target)

if __name__ == "__main__":
    main()
