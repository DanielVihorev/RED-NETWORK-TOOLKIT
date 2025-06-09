# RED-NETWORK-TOOLKIT
The script is a basic penetration testing tool designed to automate the process of testing a remote machine for vulnerabilities.

Here’s a brief explanation of what the script does:

**Summary:**  
The script is a basic penetration testing tool designed to automate the process of testing a remote machine for vulnerabilities.

**How it works:**
1. **Ping the Target:**  
   The script first checks if the target machine (IP address) is online by sending a ping request.

2. **TCP Port Scanning:**  
   If the target is up, it scans all (or a specified range of) TCP ports on the target machine to see which ports are open.

3. **SSH Brute-Force Attack:**  
   If port 22 (the default SSH port) is open, the script tries to log in by systematically testing combinations of usernames and passwords from pre-defined lists (brute-force attack).

4. **Result Reporting:**  
   If it successfully logs in, it prints out the correct username and password that allow SSH access.

**Main Technologies Used:**
- `socket` or `scapy` for network actions (pinging and port scanning)
- `paramiko` for SSH connections and brute-forcing

**Purpose:**  
This script demonstrates fundamental concepts in network security and penetration testing: host discovery, port scanning, and brute-forcing credentials. It’s typically used for educational or authorized security testing purposes only.
