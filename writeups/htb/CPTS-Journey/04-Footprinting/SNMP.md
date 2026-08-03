# SNMP (Simple Network Management Protocol)

## Overview

SNMP (Simple Network Management Protocol) is a protocol used to **monitor, manage, and configure network devices remotely**.

It is commonly found on:

- Routers
- Switches
- Servers
- Firewalls
- Printers
- IoT devices
- Access Points

SNMP allows administrators to retrieve information from devices and, depending on permissions, modify their configuration.

---

# Default Ports

| Port | Protocol | Service |
|------|----------|---------|
| **161** | UDP | SNMP Queries (GET/SET) |
| **162** | UDP | SNMP Traps |

---

# Main Components

## Manager

The client responsible for querying and managing SNMP-enabled devices.

## Agent

Software running on the managed device that responds to SNMP requests.

## MIB (Management Information Base)

A hierarchical database describing all objects that can be queried through SNMP.

## OID (Object Identifier)

A unique identifier for every object available through SNMP.

Example:

```text
.1.3.6.1.2.1.1.5.0
```

---

# SNMP Versions

## SNMPv1

- No authentication
- No encryption
- Data transmitted in plain text

---

## SNMPv2c

- Community-based authentication
- Improved functionality
- Community strings transmitted in plain text

---

## SNMPv3

- Username/password authentication
- Encryption support
- Most secure version
- More complex configuration

---

# Community Strings

Community strings function as passwords controlling access to SNMP data.

Common examples:

```text
public
private
```

Access types:

- Read Only (RO)
- Read Write (RW)

---

# Default Configuration

Configuration file:

```text
/etc/snmp/snmpd.conf
```

Example configuration:

```text
rocommunity public default
```

Default configuration defines:

- Listening addresses
- Community strings
- Accessible MIB views
- Authentication
- Agent settings

---

# Dangerous Configuration Options

| Setting | Description |
|----------|-------------|
| `rwuser noauth` | Grants full OID tree access without authentication. |
| `rwcommunity <community> <IPv4>` | Read/write access using a community string. |
| `rwcommunity6 <community> <IPv6>` | IPv6 equivalent of rwcommunity. |

---

# Common Misconfigurations

- Default community strings (`public`, `private`)
- Read-write community strings enabled
- SNMPv1/v2c used instead of SNMPv3
- Community strings transmitted in clear text
- Overly permissive OID access
- Weakly protected SNMP configuration

---

# Enumeration

## Nmap

Detect the SNMP service.

```bash
sudo nmap -sU -sV -p161 --script snmp* <TARGET>
```

Useful information obtained:

- SNMP version
- Available OIDs
- Device information
- System details

---

## snmpwalk

Enumerate available OIDs.

```bash
snmpwalk -v2c -c public <TARGET>
```

Can reveal:

- Operating System
- Hostname
- Kernel version
- Installed software
- Network interfaces
- Uptime
- System contact
- System location

---

## OneSixtyOne

Brute-force community strings.

```bash
onesixtyone -c /opt/useful/seclists/Discovery/SNMP/snmp.txt <TARGET>
```

Example output:

```text
10.129.14.128 [public]
```

---

## Braa

Fast SNMP enumeration tool.

```bash
braa public@<TARGET>:.1.3.6.*
```

Used to enumerate OIDs efficiently once a valid community string has been identified.

---

# Enumeration Workflow

1. Identify UDP port **161**.
2. Determine the SNMP version.
3. Discover valid community strings.
4. Enumerate available OIDs.
5. Identify system information.
6. Enumerate installed software and services.
7. Search for sensitive information.

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| Nmap | Service detection and NSE scripts. |
| snmpwalk | Enumerate OIDs. |
| onesixtyone | Community string brute-force. |
| braa | Fast SNMP enumeration. |

---

# Best Practices

- Prefer SNMPv3 whenever possible.
- Disable default community strings.
- Avoid read-write communities unless necessary.
- Restrict SNMP access to trusted hosts.
- Verify discovered community strings manually.
- Record useful OIDs and discovered system information.

---

# Key Takeaways

- SNMP is commonly used for monitoring and managing network devices.
- Uses **UDP 161** for queries and **UDP 162** for traps.
- **MIB** defines available objects, while **OID** uniquely identifies them.
- SNMPv1 and SNMPv2c transmit community strings in plain text.
- SNMPv3 provides authentication and encryption.
- `snmpwalk`, `onesixtyone`, `braa`, and `Nmap` are the primary enumeration tools.
- Misconfigured SNMP services can expose valuable system information during enumeration.