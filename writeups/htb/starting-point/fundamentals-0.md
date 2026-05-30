# HTB Starting Point - Service Enumeration (FTP, SMB, Telnet, Redis)

Objective: Practice basic enumeration and interaction with common services using Nmap and manual tools.

First step was running an Nmap scan to identify open ports and services:
nmap -sC -sV IP

This revealed multiple services:
FTP (21)
SMB (445)
Telnet (23)
Redis (6379)

FTP:
I tested FTP connection using:
ftp "IP"

Then I tried anonymous login:
username: anonymous
password: anonymous

This allowed access to the FTP service and file exploration.

SMB:
I enumerated SMB shares using:
smbclient -L //IP -N

I listed available shares and checked for accessible resources.

Telnet:
I connected using:
telnet IP

Telnet allowed manual interaction with the service. It is insecure because it sends data in plaintext.

Redis:
I accessed Redis using:
redis-cli -h IP

I explored the database and tested basic commands to understand how the service works.

Result:
By enumerating all services, I identified different attack surfaces:
- FTP may allow anonymous file access
- SMB may expose shared folders
- Telnet is insecure due to plaintext communication
- Redis may expose internal data if not protected

What I learned:
- Always start with full port enumeration (Nmap)
- Identify and test each service individually
- Understand how different protocols behave
- Enumeration is the most important phase in penetration testing

Conclusion:
This machine helped me understand how different services can expose vulnerabilities and why proper enumeration is critical before exploitation.