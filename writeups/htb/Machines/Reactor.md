# HTB - Reactor (Easy)

## Overview
The **Reactor** machine on Hack The Box is an easy-difficulty Linux target focused on service enumeration, exploitation of a known vulnerability, and privilege escalation.

---

## Reconnaissance
I started by performing a reconnaissance scan against the target using `nmap` in order to identify open ports and running services.

During enumeration, several exposed services were identified that could potentially be leveraged for exploitation.

---

## Exploitation and Initial Access
After analyzing the exposed services, I identified a **known vulnerability** affecting one of the target services.

I used the **Metasploit Framework (msfconsole)** to search for and configure the appropriate exploit module, setting the required parameters such as RHOST and RPORT.

After executing the exploit, I successfully obtained **initial access** to the machine, gaining a low-privileged shell.

---

## Privilege Escalation
With initial access established, I performed local enumeration to identify potential privilege escalation vectors.

During this phase, I analyzed:
- System permissions
- Misconfigurations
- Potentially vulnerable binaries

After identifying a viable misconfiguration, I was able to escalate privileges to **root**.

---

## Root Flag
With elevated privileges, I accessed the root directory and retrieved the final flag, successfully completing the machine.

---

## Learning Outcomes
- Network and service enumeration using nmap
- Exploitation of known vulnerabilities using Metasploit
- Gaining initial access to a target system
- Basic Linux privilege escalation techniques