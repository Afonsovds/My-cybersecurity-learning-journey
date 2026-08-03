# SMTP

## Overview

SMTP (Simple Mail Transfer Protocol) is the standard protocol used to **send emails** across IP networks. It is used between email clients and mail servers, as well as between mail servers themselves.

Unlike IMAP and POP3, SMTP is responsible **only for sending and relaying emails**, not retrieving them.

SMTP commonly works alongside:

- IMAP (mail retrieval & synchronization)
- POP3 (mail retrieval)

---

# Default Ports

| Port | Protocol | Description |
|------|----------|-------------|
| **25** | TCP | Standard SMTP (server-to-server communication). |
| **465** | TCP | SMTPS (SMTP over SSL/TLS). |
| **587** | TCP | SMTP Submission (authenticated users using STARTTLS). |

---

# Mail Flow

```text
Mail User Agent (MUA)
        │
        ▼
Mail Submission Agent (MSA)
        │
        ▼
Mail Transfer Agent (MTA)
        │
        ▼
Mail Delivery Agent (MDA)
        │
        ▼
Mailbox (IMAP / POP3)
```

---

# Common Use Cases

SMTP is responsible for:

- Sending emails
- Relaying emails between mail servers
- Authenticating users before sending mail
- Spam prevention
- Email routing

---

# SMTP Security

Originally SMTP sends everything in **plain text**, including:

- Usernames
- Passwords
- Email contents
- Commands

Modern implementations improve security with:

- STARTTLS
- SSL/TLS
- SMTP Authentication (SMTP AUTH)
- ESMTP extensions

---

# ESMTP

Extended SMTP (ESMTP) enhances SMTP by adding features such as:

- STARTTLS
- SMTP AUTH
- PIPELINING
- SIZE extension
- CHUNKING
- Enhanced status codes

The connection normally follows:

```text
EHLO
STARTTLS
AUTH PLAIN
MAIL FROM
RCPT TO
DATA
QUIT
```

---

# Default Configuration

Postfix configuration file:

```text
/etc/postfix/main.cf
```

Typical settings include:

- Hostname
- Allowed networks (`mynetworks`)
- Mailbox location
- TLS settings
- Listening interfaces
- SMTP banner

---

# Important Configuration Options

| Setting | Description |
|----------|-------------|
| `myhostname` | Mail server hostname. |
| `mynetworks` | Trusted IP ranges allowed to relay mail. |
| `home_mailbox` | Mailbox storage location. |
| `smtp_bind_address` | Listening IP address. |
| `inet_protocols` | IPv4 / IPv6 configuration. |
| `smtpd_banner` | SMTP banner displayed on connection. |
| `masquerade_domains` | Domain rewriting configuration. |

---

# SMTP Commands

| Command | Description |
|----------|-------------|
| `HELO` | Starts SMTP session. |
| `EHLO` | Starts ESMTP session and lists supported extensions. |
| `AUTH PLAIN` | Authenticate user. |
| `MAIL FROM` | Specify sender address. |
| `RCPT TO` | Specify recipient address. |
| `DATA` | Begin email content. |
| `RSET` | Reset current transaction. |
| `VRFY` | Verify if a mailbox exists. |
| `EXPN` | Expand mailing lists. |
| `NOOP` | Keep connection alive. |
| `QUIT` | Close connection. |

---

# Common Misconfigurations

- Open SMTP relay
- Weak authentication
- Plaintext authentication
- VRFY enabled
- EXPN enabled
- Overly permissive trusted networks
- Poor spam filtering

---

# Dangerous Configuration

Allowing every host to relay mail:

```text
mynetworks = 0.0.0.0/0
```

This creates an **Open Relay**, allowing attackers to:

- Send spam
- Spoof email addresses
- Relay malicious emails
- Abuse the mail server

---

# Enumeration

## Nmap

Identify SMTP version and supported commands.

```bash
sudo nmap -sV -sC -p25 <TARGET>
```

Useful information:

- SMTP version
- Banner
- Supported ESMTP extensions
- VRFY availability
- STARTTLS support

---

## Detect Open Relay

```bash
sudo nmap -p25 --script smtp-open-relay <TARGET>
```

Checks whether the server allows unauthenticated email relaying.

---

# Manual Enumeration

## Connect

```bash
telnet <TARGET> 25
```

---

## Identify Server

```text
HELO example.com
```

or

```text
EHLO example.com
```

Returns:

- SMTP banner
- Supported capabilities
- ESMTP extensions

---

## User Enumeration

```text
VRFY root
```

Possible responses:

- User exists
- User unknown
- False positives (depends on server configuration)

> **Note:** `VRFY` results should always be verified manually since some servers always return success.

---

# Sending an Email Manually

Example SMTP conversation:

```text
EHLO example.com

MAIL FROM:<user@example.com>

RCPT TO:<admin@example.com>

DATA

Subject: Test

Hello World

.

QUIT
```

---

# Email Headers

Email headers may reveal valuable information such as:

- Sender
- Recipient
- Subject
- Date
- Mail servers traversed
- Message ID
- MIME type
- Reply-To
- Return-Path

Headers are defined by **RFC 5322**.

---

# Enumeration Workflow

1. Identify SMTP service (25/465/587).
2. Capture SMTP banner.
3. Run EHLO to enumerate capabilities.
4. Check STARTTLS support.
5. Test VRFY / EXPN.
6. Detect Open Relay.
7. Review authentication methods.
8. Look for information disclosure in headers and banners.

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| Nmap | Service detection and NSE scripts. |
| Telnet | Manual SMTP interaction. |
| Netcat (nc) | Manual SMTP communication. |
| OpenSSL | Test SMTPS and STARTTLS connections. |
| swaks | Advanced SMTP testing and email sending. |

---

# Best Practices

- Always enumerate supported SMTP extensions.
- Verify user enumeration manually.
- Check for STARTTLS support.
- Test for Open Relay.
- Review SMTP banners for version disclosure.
- Inspect email headers for useful intelligence.
- Never rely solely on automated scan results.

---

# Key Takeaways

- SMTP is responsible for **sending and relaying emails**, not retrieving them.
- Default ports are **25**, **465**, and **587**.
- ESMTP extends SMTP with features such as **STARTTLS** and **AUTH**.
- SMTP is plaintext by default unless protected with **SSL/TLS**.
- Open Relay misconfigurations are one of the most critical SMTP vulnerabilities.
- `VRFY`, banners, and EHLO responses often provide valuable enumeration information.
- Nmap's `smtp-commands` and `smtp-open-relay` scripts are essential during SMTP enumeration.