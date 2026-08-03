# MySQL

## Overview

MySQL is an open-source relational database management system (RDBMS) developed and maintained by Oracle. It follows the client-server architecture and is commonly used to store and manage application data.

MySQL is frequently found in web applications and is a core component of the **LAMP** (Linux, Apache, MySQL, PHP) and **LEMP** (Linux, Nginx, MySQL, PHP) stacks.

---

# Default Port

| Port | Protocol | Service |
|------|----------|---------|
| **3306** | TCP | MySQL |

---

# Common Use Cases

MySQL is commonly used to store:

- User accounts
- Password hashes
- Customer information
- Website content
- Email addresses
- Permissions and roles
- Application configuration
- Metadata

---

# Common Clients

| Client | Description |
|--------|-------------|
| `mysql` | Default command-line client. |
| MySQL Workbench | Official graphical client. |
| MariaDB Client | Compatible client for MariaDB servers. |

---

# Default Configuration

Default configuration file:

```text
/etc/mysql/mysql.conf.d/mysqld.cnf
```

Important default settings:

- Runs as the **mysql** user.
- Listens on **TCP port 3306**.
- Stores databases in:

```text
/var/lib/mysql
```

- Uses Unix sockets for local communication.

---

# Important Configuration Options

| Setting | Description |
|----------|-------------|
| `user` | User running the MySQL service. |
| `password` | MySQL account password. |
| `admin_address` | Administrative listening interface. |
| `secure_file_priv` | Restricts file import/export operations. |
| `debug` | Enables debug output. |
| `sql_warnings` | Displays SQL warning messages. |

---

# Common Misconfigurations

- Weak or default credentials.
- Remote database access enabled.
- Incorrect file permissions.
- Sensitive configuration files readable by low-privileged users.
- Verbose SQL error messages.
- Insecure `secure_file_priv` configuration.

---

# Enumeration

## Nmap

Scan the MySQL service.

```bash
sudo nmap -sV -sC -p3306 --script mysql* <TARGET>
```

Useful information obtained:

- MySQL version
- Authentication plugin
- Available users
- Empty password checks
- Configuration details
- Supported capabilities

---

# Connecting to MySQL

Connect using valid credentials.

```bash
mysql -u <USER> -p<PASSWORD> -h <TARGET>
```

Example:

```bash
mysql -u root -pP4SSw0rd -h 10.10.10.10
```

> **Note:** There must be **no space** between `-p` and the password.

---

# Default Databases

| Database | Description |
|----------|-------------|
| `mysql` | User accounts and authentication information. |
| `information_schema` | Database metadata. |
| `performance_schema` | Performance monitoring. |
| `sys` | System statistics and management views. |

---

# Useful SQL Commands

## List Databases

```sql
SHOW DATABASES;
```

---

## Select Database

```sql
USE database_name;
```

---

## List Tables

```sql
SHOW TABLES;
```

---

## Show Table Columns

```sql
SHOW COLUMNS FROM table_name;
```

---

## Display Table Contents

```sql
SELECT * FROM table_name;
```

---

## Search for Specific Data

```sql
SELECT * FROM table_name
WHERE column_name = 'value';
```

---

## Display Server Version

```sql
SELECT VERSION();
```

---

# Enumeration Workflow

1. Identify the MySQL service on TCP **3306**.
2. Determine the MySQL version.
3. Test valid credentials.
4. Enumerate available databases.
5. Identify interesting tables.
6. Review table structure.
7. Extract useful information.
8. Search for credentials or sensitive data.

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| Nmap | Service detection and NSE enumeration. |
| mysql | Native MySQL client. |
| MySQL Workbench | GUI database management. |

---

# Best Practices

- Enumerate before attempting exploitation.
- Verify Nmap results manually to avoid false positives.
- Check for remote database access.
- Review system databases for useful information.
- Look for sensitive data and credential storage.
- Record all discovered databases and tables.

---

# Key Takeaways

- MySQL typically listens on **TCP port 3306**.
- It is commonly deployed as part of the **LAMP** and **LEMP** stacks.
- The `mysql` client is the standard tool for interacting with databases.
- `information_schema` and `sys` contain valuable metadata.
- Weak credentials and remote access are common attack vectors.
- Always validate automated scan results before relying on them.