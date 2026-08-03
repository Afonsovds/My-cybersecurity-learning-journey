# SMB (Server Message Block)

## Overview

Server Message Block (SMB) is a client-server protocol used for sharing files, directories, printers, and other network resources between systems. It is primarily associated with Microsoft Windows but is also supported on Linux and Unix systems through **Samba**.

SMB operates over TCP and allows authenticated users (or anonymous users if configured) to access shared resources on remote hosts.

SMB follows a client-server architecture where the client sends requests and the SMB server processes them.

---

# Default Ports

| Port | Protocol | Service |
|------|----------|---------|
| **137** | UDP | NetBIOS Name Service (NBNS) |
| **138** | UDP | NetBIOS Datagram Service |
| **139** | TCP | NetBIOS Session Service |
| **445** | TCP | SMB over TCP (Direct Hosting) |

---

# SMB Versions

| Version | Supported Since | Features |
|---------|-----------------|----------|
| CIFS | Windows NT 4.0 | SMB over NetBIOS |
| SMB 1.0 | Windows 2000 | Direct TCP support |
| SMB 2.0 | Windows Vista / Server 2008 | Performance improvements, caching |
| SMB 2.1 | Windows 7 / Server 2008 R2 | Locking mechanisms |
| SMB 3.0 | Windows 8 / Server 2012 | Encryption, multichannel, remote storage |
| SMB 3.0.2 | Windows 8.1 / Server 2012 R2 | Bug fixes |
| SMB 3.1.1 | Windows 10 / Server 2016 | Integrity checking, AES-128 encryption |

---

# Samba

Samba is the open-source implementation of the SMB protocol for Linux and Unix systems.

Features include:

- SMB/CIFS file sharing
- Active Directory integration
- Domain Controller functionality (Samba 4+)
- Cross-platform interoperability with Windows

Main daemons:

| Daemon | Purpose |
|---------|---------|
| smbd | File and printer sharing |
| nmbd | NetBIOS name service |

---

# SMB Authentication

SMB may allow:

- Authenticated access
- Guest access
- Anonymous (Null Session)

Access permissions are controlled through:

- Access Control Lists (ACLs)
- Share permissions
- File system permissions

---

# Default Samba Configuration

Configuration file:

```text
/etc/samba/smb.conf
```

Common configuration:

```ini
[global]
workgroup = WORKGROUP
server string = Samba Server
map to guest = bad user
usershare allow guests = yes
```

---

# Important Configuration Options

| Setting | Description |
|----------|-------------|
| workgroup | SMB workgroup/domain |
| server string | Server description |
| path | Shared directory |
| browseable | Show share during enumeration |
| guest ok | Allow anonymous access |
| read only | Read-only share |
| writable | Allow writing |
| create mask | Default file permissions |
| directory mask | Default directory permissions |
| unix password sync | Synchronize UNIX password |
| map to guest | Guest authentication behavior |

---

# Dangerous Configuration Options

| Setting | Risk |
|----------|------|
| guest ok = yes | Anonymous access |
| browseable = yes | Share enumeration |
| writable = yes | File upload/modification |
| read only = no | Allows modifications |
| create mask = 0777 | World writable files |
| directory mask = 0777 | World writable directories |
| enable privileges = yes | Honors SID privileges |
| logon script | Executes script at login |
| magic script | Executes arbitrary script |

---

# Common Shares

| Share | Purpose |
|--------|---------|
| IPC$ | Inter-process communication |
| print$ | Printer drivers |
| home | User home directories |
| NETLOGON | Login scripts |
| SYSVOL | Active Directory policies |

---

# Common Misconfigurations

- Anonymous access enabled
- Guest writable shares
- World writable permissions (0777)
- Sensitive files inside shares
- SMB signing disabled
- SMBv1 enabled
- Excessive share permissions
- Improper ACL configuration

---

# Enumeration

## Nmap

Basic SMB enumeration:

```bash
sudo nmap -sV -sC -p139,445 <TARGET>
```

Run SMB NSE scripts:

```bash
sudo nmap --script smb* -p139,445 <TARGET>
```

Useful information obtained:

- SMB version
- OS version
- SMB signing
- NetBIOS name
- Supported dialects

---

## SMBClient

List available shares anonymously:

```bash
smbclient -N -L //<TARGET>
```

Authenticate:

```bash
smbclient //<TARGET>/<SHARE> -U <USER>
```

Anonymous login:

```bash
smbclient //<TARGET>/<SHARE>
```

Useful commands:

```text
help
ls
dir
cd
pwd
get file.txt
mget *
put file.txt
mkdir folder
rm file
exit
```

Download a file:

```bash
get filename.txt
```

Execute local command:

```bash
!ls
```

---

## RPCClient

Anonymous connection:

```bash
rpcclient -U "" <TARGET>
```

Null session:

```bash
rpcclient -N -U "" <TARGET>
```

Useful commands:

| Command | Description |
|----------|-------------|
| srvinfo | Server information |
| enumdomains | Enumerate domains |
| querydominfo | Domain information |
| netshareenumall | Enumerate shares |
| netsharegetinfo <share> | Share details |
| enumdomusers | Enumerate users |
| queryuser <RID> | User information |
| querygroup <RID> | Group information |

Examples:

```text
srvinfo
```

```text
enumdomains
```

```text
enumdomusers
```

```text
netshareenumall
```

```text
queryuser 0x3e8
```

---

## RID Brute Force

Enumerate users by RID:

```bash
for i in $(seq 500 1100); do
rpcclient -N -U "" <TARGET> \
-c "queryuser 0x$(printf '%x\n' $i)" \
| grep "User Name\|user_rid\|group_rid"
done
```

---

## Impacket Samrdump

```bash
samrdump.py <TARGET>
```

Useful information:

- Usernames
- RID
- Password age
- Account status
- Group membership

---

## SMBMap

Enumerate shares:

```bash
smbmap -H <TARGET>
```

Authenticate:

```bash
smbmap -H <TARGET> -u <USER> -p <PASSWORD>
```

Shows:

- Share names
- Read permissions
- Write permissions

---

## CrackMapExec

Enumerate shares anonymously:

```bash
crackmapexec smb <TARGET> --shares -u '' -p ''
```

Authenticate:

```bash
crackmapexec smb <TARGET> -u <USER> -p <PASSWORD> --shares
```

Useful modules:

```bash
--users
```

```bash
--groups
```

```bash
--sessions
```

```bash
--loggedon-users
```

---

## Enum4Linux-ng

Installation:

```bash
git clone https://github.com/cddmp/enum4linux-ng.git

cd enum4linux-ng

pip3 install -r requirements.txt
```

Enumeration:

```bash
./enum4linux-ng.py <TARGET> -A
```

Collects:

- Users
- Groups
- Shares
- Policies
- Password policy
- SMB dialects
- OS information
- NetBIOS information

---

# Enumeration Workflow

1. Identify SMB ports (139/445).
2. Determine SMB version.
3. Check SMB signing.
4. Test anonymous access.
5. Enumerate shares.
6. Inspect share permissions.
7. Download interesting files.
8. Enumerate users.
9. Enumerate groups.
10. Enumerate password policy.
11. Perform RID brute force.
12. Look for credentials and sensitive data.

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| Nmap | Service detection and SMB NSE scripts |
| smbclient | Access SMB shares |
| rpcclient | RPC enumeration |
| smbmap | Share permissions |
| CrackMapExec | SMB enumeration and validation |
| enum4linux-ng | Automated SMB enumeration |
| samrdump.py | User enumeration via SAMR |

---

# Best Practices

- Check for Null Sessions.
- Enumerate shares before authentication.
- Verify anonymous access manually.
- Inspect writable shares.
- Download configuration files.
- Enumerate users before password attacks.
- Check SMB signing.
- Identify SMB version.
- Use multiple tools to validate results.

---

# Key Takeaways

- SMB primarily operates on **TCP 445** and **TCP 139**.
- Samba provides SMB support on Linux and Unix.
- Anonymous access can expose users, shares, and sensitive information.
- `rpcclient` is one of the most powerful manual enumeration tools.
- `enum4linux-ng` automates much of the enumeration process.
- Writable shares often lead to privilege escalation or code execution.
- Always verify automated tool results manually.