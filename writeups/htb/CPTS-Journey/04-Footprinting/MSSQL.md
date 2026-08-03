# Microsoft SQL Server (MSSQL)

## Overview

Microsoft SQL Server (MSSQL) is Microsoft's relational database management system (RDBMS). Unlike MySQL, MSSQL is closed-source and is primarily designed for Windows environments, although Linux and macOS versions are also available.

MSSQL is widely used in enterprise environments and integrates natively with the **.NET Framework**, making it a common target during internal penetration tests.

---

# Default Port

| Port | Protocol | Service |
|------|----------|---------|
| **1433** | TCP | Microsoft SQL Server |

---

# Common Clients

Several clients can be used to interact with MSSQL databases.

| Client | Description |
|--------|-------------|
| SQL Server Management Studio (SSMS) | Microsoft's official graphical management tool. |
| mssqlclient.py | Impacket client commonly used by penetration testers. |
| mssql-cli | Command-line MSSQL client. |
| SQL Server PowerShell | PowerShell management interface. |
| HeidiSQL | Third-party database client. |
| SQLPro | Cross-platform SQL client. |

---

# Default System Databases

| Database | Purpose |
|----------|---------|
| **master** | Stores system-wide configuration and metadata. |
| **model** | Template used when creating new databases. |
| **msdb** | Stores SQL Server Agent jobs, alerts, and schedules. |
| **tempdb** | Temporary storage for queries and objects. |
| **resource** | Read-only database containing system objects. |

---

# Default Configuration

By default:

- MSSQL runs as **NT SERVICE\MSSQLSERVER**
- Windows Authentication is commonly enabled.
- SQL communication may not enforce encryption.
- Active Directory authentication is often supported.

---

# Common Misconfigurations

- Weak or default **sa** passwords.
- Encryption disabled.
- Self-signed TLS certificates.
- Named Pipes enabled.
- Excessive database privileges.

---

# Enumeration

## Nmap

Identify the MSSQL service and collect version information.

```bash
sudo nmap -sV -p1433 <TARGET>
```

---

## Nmap NSE Scripts

Useful scripts for MSSQL enumeration:

```bash
sudo nmap \
--script ms-sql-info,ms-sql-config,ms-sql-empty-password,\
ms-sql-ntlm-info,ms-sql-tables,\
ms-sql-hasdbaccess,ms-sql-dump-hashes \
-p1433 <TARGET>
```

These scripts can reveal:

- SQL Server version
- Instance name
- NTLM information
- Named Pipes
- Accessible databases
- Weak or empty passwords
- Password hashes (when permitted)

---

## Metasploit

Identify MSSQL instances.

```bash
use auxiliary/scanner/mssql/mssql_ping

set RHOSTS <TARGET>

run
```

This module provides:

- Server name
- Instance name
- SQL version
- Listening port
- Named Pipes
- Cluster information

---

# Connecting with Impacket

Connect using Windows Authentication.

```bash
python3 mssqlclient.py Administrator@<TARGET> -windows-auth
```

After authentication, an interactive SQL shell becomes available.

---

# Useful SQL Queries

## List Databases

```sql
SELECT name FROM sys.databases;
```

---

## List Current User

```sql
SELECT SYSTEM_USER;
```

---

## Show Server Version

```sql
SELECT @@VERSION;
```

---

## List Current Database

```sql
SELECT DB_NAME();
```

---

## List Tables

```sql
SELECT * FROM INFORMATION_SCHEMA.TABLES;
```

---

# Enumeration Workflow

1. Identify the MSSQL service on TCP **1433**.
2. Detect SQL Server version.
3. Identify the database instance.
4. Check authentication methods.
5. Test for weak credentials.
6. Connect using **mssqlclient.py**.
7. Enumerate databases, tables, and users.
8. Assess user privileges.

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| Nmap | Service detection and NSE enumeration. |
| Metasploit | MSSQL discovery and auxiliary modules. |
| Impacket mssqlclient.py | Interactive MSSQL client. |
| SQL Server Management Studio | Administrative interface. |

---

# Best Practices

- Enumerate SQL Server version and instance names.
- Check whether Windows Authentication is enabled.
- Test weak or default credentials.
- Enumerate available databases before exploitation.
- Record Named Pipes and NTLM information.
- Identify privilege levels after authentication.

---

# Key Takeaways

- MSSQL typically listens on **TCP port 1433**.
- Windows Authentication is commonly used.
- The **master** database stores system information.
- **mssqlclient.py** is one of the most useful tools for MSSQL enumeration.
- Nmap NSE scripts provide valuable information about SQL Server instances.
- Weak **sa** credentials and misconfigurations are common attack vectors.
- Successful authentication allows direct interaction with databases using T-SQL.