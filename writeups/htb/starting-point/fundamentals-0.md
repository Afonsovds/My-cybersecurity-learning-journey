# HTB Starting Point - Fundamentals 0: Service Enumeration (FTP, SMB, Telnet, Redis)

## Objective: Learn how to identify and interact with common network services through enumeration and manual exploration.

I started by performing an Nmap scan to identify open ports and determine which services were running on the target.
```bash
nmap -sC -sV IP
```

The scan revealed several services, including FTP, SMB, Telnet and Redis. Instead of focusing on exploitation, this module emphasized understanding how these services work and how to interact with them safely.

## FTP:
I connected to the FTP service and tested anonymous authentication.
```bash
ftp IP
```
Using the anonymous account, I explored the available files and directories. This demonstrated how misconfigured file transfer services can unintentionally expose information.

## SMB:
I enumerated the available SMB shares using:
```bash
smbclient -L //IP -N
```
I reviewed the accessible shares and learned how file-sharing services can reveal useful information during an assessment.

## Telnet:
I connected to the Telnet service to understand how remote administration worked before more secure alternatives became standard.
```bash
telnet IP
```
This highlighted one of Telnet's main weaknesses: all communication is transmitted in plaintext.

## Redis:
I accessed the Redis service and explored its basic functionality.
```bash
redis-cli -h IP
```
This exercise introduced me to in-memory databases and demonstrated the risks of exposing services without proper access controls.

## Result:
Through the enumeration and exploration of multiple services, I gained a better understanding of how different technologies operate and how they may contribute to an attack surface when improperly configured.

What I learned:

* How to identify services using Nmap.
* How to interact with FTP, SMB, Telnet and Redis.
* Why exposed services should be properly secured.
* The importance of understanding a service before attempting exploitation.
* That enumeration is one of the most valuable phases of a penetration test.

Conclusion:
This module reinforced that effective penetration testing begins with curiosity and observation. Learning how common services behave and how to interact with them provides the foundation needed for more advanced security assessments in the future.
