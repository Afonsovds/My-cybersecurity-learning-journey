# Oracle TNS (Transparent Network Substrate)

## Overview

Oracle Transparent Network Substrate (TNS) is the communication protocol used by Oracle databases to enable communication between database instances and client applications over a network.

It provides secure and reliable connectivity while supporting features such as:

- Name resolution
- Connection management
- Load balancing
- SSL/TLS encryption
- Performance monitoring

Oracle databases are widely deployed in enterprise environments, making Oracle TNS an important target during internal penetration tests.

---

# Default Port

| Port | Protocol | Service |
|------|----------|---------|
| **1521** | TCP | Oracle TNS Listener |

---

# Key Configuration Files

| File | Description |
|------|-------------|
| `tnsnames.ora` | Client-side configuration used to resolve Oracle services. |
| `listener.ora` | Server-side configuration defining listener behavior and available services. |

These files are usually located in:

```text
$ORACLE_HOME/network/admin
```

---

# Important Parameters

| Parameter | Description |
|-----------|-------------|
| `HOST` | Database server hostname or IP address. |
| `PORT` | Listener port (default 1521). |
| `SERVICE_NAME` | Database service name. |
| `SID` | Unique identifier of a database instance. |
| `USER` | Username used for authentication. |
| `PASSWORD` | Password used for authentication. |

---

# Enumeration

## Nmap

Identify the Oracle TNS listener.

```bash
sudo nmap -sV -p1521 <TARGET>
```  

---

## SID Enumeration

Brute-force Oracle SIDs using the Nmap NSE script.

```bash
sudo nmap -p1521 --script oracle-sid-brute <TARGET>
```

Example output:

```text
XE
```

---

## Oracle Database Attacking Tool (ODAT)

ODAT is an open-source framework used to enumerate and assess Oracle databases.

Run all available checks:

```bash
./odat.py all -s <TARGET>
```

ODAT can identify:

- Database version
- Valid credentials
- Running services
- Database users
- Misconfigurations
- Known vulnerabilities

---

# Default Credentials

Some Oracle installations may still use default credentials.

Examples:

| Username | Password |
|----------|----------|
| `scott` | `tiger` |
| `dbsnmp` | `dbsnmp` |
| `SYS` | Administrator account |

Older Oracle versions may also contain default passwords.

---

# Connecting with SQL*Plus

Connect to an Oracle database.

```bash
sqlplus username/password@TARGET/SID
```

Example:

```bash
sqlplus scott/tiger@10.10.10.10/XE
```

---

# Useful SQL Queries

## List Tables

```sql
SELECT table_name FROM all_tables;
```

---

## Show Current User Roles

```sql
SELECT * FROM user_role_privs;
```

---

## Dump Password Hashes (SYS Privileges Required)

```sql
SELECT name, password FROM sys.user$;
```

The extracted hashes can be cracked offline using tools such as Hashcat or John the Ripper.

---

# File Upload with ODAT

If the database has sufficient privileges and a web server is present, files can be uploaded.

Example:

```bash
./odat.py utlfile \
-s <TARGET> \
-d XE \
-U scott \
-P tiger \
--sysdba \
--putFile C:\\inetpub\\wwwroot testing.txt ./testing.txt
```

Verify the upload:

```bash
curl http://<TARGET>/testing.txt
```

---

# Common Web Server Paths

| Operating System | Default Web Root |
|------------------|------------------|
| Linux | `/var/www/html` |
| Windows | `C:\inetpub\wwwroot` |

---

# Common Enumeration Workflow

1. Identify the Oracle listener on port **1521**.
2. Enumerate available **SIDs**.
3. Test for default or weak credentials.
4. Connect using **SQL*Plus**.
5. Enumerate tables, users, and roles.
6. Check for administrative privileges.
7. Dump password hashes if possible.
8. Attempt file upload or further exploitation when permissions allow.

---

# Best Practices

- Always enumerate the Oracle listener before attacking the database.
- Identify valid SIDs before attempting authentication.
- Test for default credentials.
- Use ODAT to automate enumeration.
- Review user privileges after authentication.
- Look for opportunities to extract password hashes.
- Verify whether file upload functionality is available.

---

# Key Takeaways

- Oracle TNS uses **TCP port 1521** by default.
- `SID` identifies a specific Oracle database instance.
- `tnsnames.ora` and `listener.ora` are the primary configuration files.
- ODAT is one of the most valuable tools for Oracle database enumeration.
- SQL*Plus allows direct interaction with Oracle databases.
- Administrative privileges may allow password hash extraction and file uploads.
- Oracle databases are common targets during internal penetration testing.