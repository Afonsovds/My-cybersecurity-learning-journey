# 🛰️ Nmap Reference Guide

> A comprehensive reference guide for **Nmap**, covering the essential concepts, scan types, options, examples, and best practices used throughout the CPTS learning path.

---

# What is Nmap?

**Nmap (Network Mapper)** is an open-source network discovery and security auditing tool used to identify live hosts, discover open ports, detect running services, identify operating systems, and perform security assessments.

---

# Basic Syntax

```bash
nmap [Scan Type] [Options] <Target>
```

Example:

```bash
nmap -sV -sC 10.10.10.10
```

---

# Target Specification

| Example           | Description            |
| ----------------- | ---------------------- |
| `10.10.10.10`     | Single host            |
| `10.10.10.0/24`   | Entire subnet          |
| `192.168.1.10-20` | IP range               |
| `example.com`     | Domain                 |
| `target1 target2` | Multiple targets       |
| `-iL targets.txt` | Read targets from file |

---

# Host Discovery

| Option               | Description                            |
| -------------------- | -------------------------------------- |
| `-sn`                | Ping scan only (disable port scanning) |
| `-Pn`                | Skip host discovery                    |
| `-PE`                | ICMP Echo Request                      |
| `-PP`                | ICMP Timestamp Request                 |
| `-PM`                | ICMP Address Mask Request              |
| `-PR`                | ARP Ping (local network)               |
| `-n`                 | Disable DNS resolution                 |
| `--disable-arp-ping` | Disable ARP discovery                  |

---

# Port Scanning

| Option            | Description                |
| ----------------- | -------------------------- |
| `-p-`             | Scan all 65,535 ports      |
| `-p22,80,443`     | Scan specific ports        |
| `-p22-1000`       | Scan a port range          |
| `--top-ports 100` | Scan the most common ports |
| `-F`              | Fast scan (Top 100 ports)  |

---

# Scan Types

| Option | Description            |
| ------ | ---------------------- |
| `-sS`  | TCP SYN Scan (Stealth) |
| `-sT`  | TCP Connect Scan       |
| `-sU`  | UDP Scan               |
| `-sA`  | ACK Scan               |
| `-sN`  | NULL Scan              |
| `-sF`  | FIN Scan               |
| `-sX`  | Xmas Scan              |
| `-sI`  | Idle Scan              |

---

# Service Enumeration

| Option              | Description                                                 |
| ------------------- | ----------------------------------------------------------- |
| `-sV`               | Detect service versions                                     |
| `-sC`               | Run default NSE scripts                                     |
| `--script=<script>` | Execute a specific NSE script                               |
| `--script=vuln`     | Run vulnerability scripts                                   |
| `--script=safe`     | Run safe scripts                                            |
| `-A`                | Enable OS detection, version detection, NSE, and traceroute |

---

# Operating System Detection

| Option           | Description                              |
| ---------------- | ---------------------------------------- |
| `-O`             | Detect the operating system              |
| `--osscan-guess` | Guess the OS when detection is uncertain |

---

# Firewall Evasion

| Option           | Description               |
| ---------------- | ------------------------- |
| `-D RND:5`       | Use five random decoys    |
| `-S <IP>`        | Spoof source IP           |
| `-e <interface>` | Specify network interface |
| `-g <port>`      | Specify source port       |
| `--spoof-mac`    | Spoof MAC address         |
| `-f`             | Fragment packets          |

---

# Performance

| Option             | Description                      |
| ------------------ | -------------------------------- |
| `-T0`              | Paranoid                         |
| `-T1`              | Sneaky                           |
| `-T2`              | Polite                           |
| `-T3`              | Normal                           |
| `-T4`              | Aggressive                       |
| `-T5`              | Insane                           |
| `--min-rate`       | Minimum packet rate              |
| `--max-retries`    | Maximum retries                  |
| `-v` / `-vv`       | Verbose output                   |
| `--stats-every 5s` | Display progress every 5 seconds |

---

# Output Formats

| Option     | Description         |
| ---------- | ------------------- |
| `-oA scan` | Save in all formats |
| `-oN scan` | Normal output       |
| `-oG scan` | Grepable output     |
| `-oX scan` | XML output          |

---

# Port States

| State               | Description                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Open**            | A service is actively listening on the port.                                                                   |
| **Closed**          | The host is reachable, but no service is listening.                                                            |
| **Filtered**        | A firewall or packet filter prevents Nmap from determining the port state.                                     |
| **Unfiltered**      | The port is reachable, but Nmap cannot determine whether it is open or closed. Only reported during ACK scans. |
| **Open|Filtered**   | No response was received, making it impossible to determine whether the port is open or filtered.              |
| **Closed|Filtered** | Only appears during Idle scans when Nmap cannot determine whether the port is closed or filtered.              |

---

# Common Commands

## Host Discovery

```bash
nmap -sn 10.10.10.0/24
```

## SYN Scan

```bash
nmap -sS 10.10.10.10
```

## Version Detection

```bash
nmap -sV 10.10.10.10
```

## Default Enumeration

```bash
nmap -sC -sV 10.10.10.10
```

## Aggressive Scan

```bash
nmap -A 10.10.10.10
```

## UDP Scan

```bash
nmap -sU 10.10.10.10
```

## Full TCP Scan

```bash
nmap -p- 10.10.10.10
```

## Scan Top 100 Ports

```bash
nmap --top-ports 100 10.10.10.10
```

## Save Results

```bash
nmap -oA scan 10.10.10.10
```

---

# Best Practices

* Start with **Host Discovery** before scanning ports.
* Enumerate **all TCP ports** (`-p-`) whenever possible.
* Combine **`-sC`** and **`-sV`** for service enumeration.
* Save scan results using **`-oA`**.
* Use **UDP scans** only when necessary, as they are slower.
* Review NSE scripts before executing intrusive categories.
* Verify findings manually instead of relying solely on automated scans.

---

# Scan Workflow

```text
Host Discovery
        │
        ▼
TCP Port Scan
        │
        ▼
Service Version Detection
        │
        ▼
NSE Script Enumeration
        │
        ▼
Operating System Detection
        │
        ▼
Manual Enumeration
```

---

# Key Takeaways

* Nmap is the foundation of network enumeration.
* Always identify live hosts before scanning ports.
* Service enumeration is more valuable than simply finding open ports.
* Understanding port states helps interpret scan results accurately.
* Save every scan for future analysis and reporting.
* Never rely exclusively on automated results—always validate manually.
