# NFS

## Overview

Network File System (NFS) is a distributed file system protocol developed by Sun Microsystems that allows Linux and Unix systems to access remote directories as if they were stored locally. Unlike SMB, NFS is primarily designed for Unix/Linux environments and uses the ONC-RPC (Open Network Computing Remote Procedure Call) protocol.

Authentication differs between versions:

- **NFSv2/v3** authenticate the client machine.
- **NFSv4** authenticates individual users and supports stronger security features such as Kerberos.

---

# Default Ports

| Port | Protocol | Service |
|------|----------|---------|
| **111** | TCP/UDP | rpcbind / Portmapper |
| **2049** | TCP/UDP | NFS |

> **Note:** NFSv4 primarily uses only **TCP 2049**, simplifying firewall configurations.

---

# NFS Versions

| Version | Features |
|----------|----------|
| **NFSv2** | Legacy version, UDP-based. |
| **NFSv3** | Better performance, larger file support, improved error handling. |
| **NFSv4** | Stateful protocol, Kerberos authentication, ACLs, firewall-friendly, improved security. |
| **NFSv4.1** | Adds pNFS (Parallel NFS), multipathing, clustering support, scalability improvements. |

---

# Common Use Cases

NFS is commonly used for:

- Shared Linux home directories
- Centralized storage
- Backup repositories
- Software repositories
- Virtual machine storage
- Development environments
- Shared application data

---

# Authentication

NFS generally relies on:

- UNIX UID
- UNIX GID
- Group memberships
- RPC authentication

Unlike SMB, authentication is not built directly into the NFS protocol.

---

# Default Configuration

Main exports configuration file:

```text
/etc/exports
```

Example:

```text
/mnt/nfs 10.129.14.0/24(sync,no_subtree_check)
```

This exports `/mnt/nfs` to every host within the subnet.

---

# Important Configuration Options

| Option | Description |
|----------|-------------|
| rw | Read and write access. |
| ro | Read-only access. |
| sync | Synchronous writes (safer). |
| async | Asynchronous writes (faster). |
| secure | Requires ports below 1024. |
| insecure | Allows ports above 1024. |
| root_squash | Maps root user to anonymous user. |
| no_root_squash | Root retains UID 0 on mounted share. |
| no_subtree_check | Disables subtree validation. |
| nohide | Exposes mounted child filesystems. |

---

# Dangerous Settings

| Setting | Risk |
|----------|------|
| rw | Allows remote file modification. |
| insecure | Allows unprivileged clients to connect. |
| no_root_squash | Root users keep full privileges. |
| nohide | Exposes nested filesystems. |

---

# Common Misconfigurations

- World-accessible exports.
- Writable shares.
- `no_root_squash` enabled.
- `insecure` enabled.
- Sensitive backups exported.
- SSH keys stored inside shares.
- Weak export restrictions.

---

# Enumeration

## Nmap

Basic scan:

```bash
sudo nmap -sV -sC -p111,2049 <TARGET>
```

RPC enumeration:

```bash
sudo nmap --script rpcinfo -p111,2049 <TARGET>
```

NFS enumeration:

```bash
sudo nmap --script nfs* -p111,2049 <TARGET>
```

Useful information obtained:

- NFS version
- Exported shares
- RPC services
- Mount permissions
- File listings
- Filesystem statistics

---

# RPC Enumeration

List RPC services:

```bash
rpcinfo -p <TARGET>
```

Useful to identify:

- rpcbind
- mountd
- nlockmgr
- nfs_acl
- NFS versions

---

# Show Exported Shares

```bash
showmount -e <TARGET>
```

Example:

```bash
showmount -e 10.10.10.10
```

Example output:

```text
Export list for 10.10.10.10:
/mnt/nfs 10.10.10.0/24
```

---

# Mounting an NFS Share

Create a mount directory:

```bash
mkdir target-NFS
```

Mount the share:

```bash
sudo mount -t nfs <TARGET>:/ ./target-NFS -o nolock
```

Example:

```bash
sudo mount -t nfs 10.10.10.10:/ ./target-NFS -o nolock
```

---

# Inspecting Files

List files:

```bash
ls -la
```

View directory tree:

```bash
tree
```

Display usernames:

```bash
ls -l
```

Display UIDs/GIDs:

```bash
ls -n
```

---

# Unmounting

```bash
sudo umount ./target-NFS
```

---

# Enumeration Workflow

1. Detect ports **111** and **2049**.
2. Identify NFS version.
3. Enumerate RPC services.
4. List exported shares.
5. Mount accessible exports.
6. Inspect file permissions.
7. Identify usernames and UIDs.
8. Search for credentials, SSH keys, backups, or sensitive files.
9. Check if `no_root_squash` is enabled.
10. Look for privilege escalation opportunities.

---

# Useful Files

| File | Purpose |
|------|---------|
| /etc/exports | Exported NFS shares. |
| /etc/fstab | Persistent mounts. |

---

# Useful Commands

## List Exports

```bash
showmount -e <TARGET>
```

---

## List RPC Services

```bash
rpcinfo -p <TARGET>
```

---

## Mount Share

```bash
sudo mount -t nfs <TARGET>:/ ./target-NFS -o nolock
```

---

## List Files

```bash
ls -la
```

---

## Display UIDs

```bash
ls -n
```

---

## Unmount

```bash
sudo umount ./target-NFS
```

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| Nmap | Service and NFS enumeration. |
| showmount | Display exported shares. |
| rpcinfo | Enumerate RPC services. |
| mount | Mount NFS exports. |
| tree | Browse directory structure. |
| ls | View permissions and ownership. |

---

# Privilege Escalation Opportunities

Potential findings include:

- Private SSH keys (`id_rsa`)
- Backup scripts
- Configuration files
- Writable shares
- Password files
- Backup archives
- SUID binaries
- `no_root_squash` exploitation
- UID/GID impersonation

---

# Best Practices

- Enumerate exports before mounting.
- Check all exported directories.
- Review file ownership using UIDs.
- Search for SSH keys and backups.
- Inspect permissions carefully.
- Test for `no_root_squash`.
- Unmount shares after enumeration.
- Record exported directories and permissions.

---

# Key Takeaways

- NFS primarily uses **TCP/UDP 111** (rpcbind) and **2049** (NFS).
- `/etc/exports` defines exported directories and permissions.
- `showmount` is the quickest way to enumerate exports.
- Nmap NSE scripts can automatically discover shares and permissions.
- `no_root_squash` is one of the most dangerous NFS misconfigurations.
- UID/GID mappings are critical when assessing access rights.
- Mounted shares often contain SSH keys, backups, and sensitive files.
- Always inspect file ownership, permissions, and export options before attempting exploitation.