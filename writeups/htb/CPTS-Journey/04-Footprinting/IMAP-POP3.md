# IMAP / POP3

## Overview

**IMAP (Internet Message Access Protocol)** and **POP3 (Post Office Protocol v3)** are email retrieval protocols used by clients to access messages stored on a mail server.

- **IMAP** allows users to manage emails directly on the server while keeping all clients synchronized.
- **POP3** is a simpler protocol that downloads emails from the server and primarily supports listing, retrieving, and deleting messages.

SMTP is typically used for sending emails, while IMAP and POP3 are used for receiving them.

---

# Default Ports

| Port | Protocol | Service |
|------|----------|---------|
| **110** | TCP | POP3 |
| **995** | TCP | POP3 over SSL/TLS |
| **143** | TCP | IMAP |
| **993** | TCP | IMAP over SSL/TLS |

---

# IMAP vs POP3

| IMAP | POP3 |
|------|------|
| Emails remain on the server. | Emails are usually downloaded locally. |
| Supports folder structures. | No folder support. |
| Synchronizes multiple devices. | Designed for a single client. |
| Allows server-side email management. | Only retrieves and deletes emails. |
| Requires an active connection for management. | Can work offline after downloading. |

---

# Common Use Cases

### IMAP

- Enterprise email systems
- Multi-device synchronization
- Shared mailboxes
- Server-side folder management
- Long-term email storage

### POP3

- Local email storage
- Simple mail clients
- Limited server storage
- Offline email access

---

# Default Configuration

Common Dovecot packages:

```bash
dovecot-imapd
dovecot-pop3d
```

Configuration is highly customizable through the Dovecot configuration files.

---

# Common IMAP Commands

| Command | Description |
|----------|-------------|
| `LOGIN username password` | Authenticate user. |
| `LIST "" *` | List mailboxes. |
| `CREATE "INBOX"` | Create mailbox. |
| `DELETE "INBOX"` | Delete mailbox. |
| `RENAME old new` | Rename mailbox. |
| `LSUB "" *` | List subscribed folders. |
| `SELECT INBOX` | Select mailbox. |
| `UNSELECT INBOX` | Exit selected mailbox. |
| `FETCH <ID> all` | Retrieve email contents. |
| `CLOSE` | Close mailbox. |
| `LOGOUT` | Disconnect. |

---

# Common POP3 Commands

| Command | Description |
|----------|-------------|
| `USER username` | Specify username. |
| `PASS password` | Authenticate user. |
| `STAT` | Number of stored emails. |
| `LIST` | List all messages. |
| `RETR id` | Retrieve email. |
| `DELE id` | Delete email. |
| `CAPA` | Display server capabilities. |
| `RSET` | Reset session state. |
| `QUIT` | Disconnect. |

---

# Important Configuration Options

| Setting | Description |
|----------|-------------|
| `auth_debug` | Enable authentication debug logging. |
| `auth_debug_passwords` | Log submitted passwords. |
| `auth_verbose` | Log failed authentication attempts. |
| `auth_verbose_passwords` | Log passwords used during authentication. |
| `auth_anonymous_username` | Username used for anonymous authentication. |

---

# Common Misconfigurations

- Plaintext authentication enabled.
- Unencrypted IMAP/POP3 sessions.
- Anonymous authentication enabled.
- Excessive authentication logging.
- Passwords stored in debug logs.
- Weak or reused user credentials.
- Self-signed certificates accepted without validation.

---

# Enumeration

## Nmap

Detect IMAP and POP3 services.

```bash
sudo nmap -sV -sC -p110,143,993,995 <TARGET>
```

Useful information obtained:

- Mail server software
- Service version
- SSL/TLS certificates
- Supported authentication methods
- Supported capabilities
- Common Name (CN)
- Organization information

---

# Enumerating with cURL

Authenticate to an IMAP server.

```bash
curl -k 'imaps://<TARGET>' --user <USER>:<PASSWORD>
```

Example:

```bash
curl -k 'imaps://10.10.10.10' --user robin:robin
```

Use verbose mode for additional details:

```bash
curl -k -v 'imaps://<TARGET>' --user <USER>:<PASSWORD>
```

Useful information obtained:

- TLS version
- SSL certificate
- IMAP banner
- Supported capabilities
- Existing mailboxes

---

# Enumerating with OpenSSL

## IMAPS

```bash
openssl s_client -connect <TARGET>:993
```

## POP3S

```bash
openssl s_client -connect <TARGET>:995
```

Useful information obtained:

- TLS version
- Cipher suite
- SSL certificate
- Mail server banner
- Authentication methods

---

# Enumeration Workflow

1. Scan ports **110**, **143**, **993**, and **995**.
2. Identify the mail server software.
3. Inspect SSL/TLS certificates.
4. Review supported capabilities.
5. Obtain valid credentials.
6. Authenticate to the service.
7. Enumerate available mailboxes.
8. Read or retrieve emails.
9. Search for credentials or sensitive information.

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| Nmap | Service detection and NSE enumeration. |
| curl | Authenticate and enumerate IMAP. |
| OpenSSL | Manual TLS interaction. |
| ncat | Interactive encrypted connections. |

---

# Best Practices

- Always enumerate both encrypted and unencrypted ports.
- Inspect SSL certificates for useful information.
- Review server capabilities before interacting.
- Test recovered credentials against IMAP and POP3.
- Search mailboxes for credentials, internal documents, or sensitive information.
- Verify manual interaction instead of relying solely on automated scans.

---

# Key Takeaways

- **IMAP** provides full server-side mailbox management and synchronization.
- **POP3** is a simpler protocol focused on downloading emails.
- Standard ports are **143/993** for IMAP and **110/995** for POP3.
- SSL/TLS versions expose certificates and server metadata useful during enumeration.
- Valid credentials can provide direct access to sensitive emails and internal information.
- Misconfigurations such as plaintext authentication, verbose logging, or weak credentials can expose valuable information during penetration testing.