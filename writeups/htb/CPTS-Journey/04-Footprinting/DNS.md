# DNS

## Overview

The **Domain Name System (DNS)** is responsible for translating **domain names** into **IP addresses**, allowing users to access services using human-readable names instead of numeric IPs.

DNS is a **distributed hierarchical system** with no central database. Information is spread across thousands of DNS servers worldwide.

Besides hostname resolution, DNS also stores information about mail servers, name servers, aliases, and other service-related records.

---

# Default Port

| Port | Protocol | Service |
|------|----------|---------|
| **53** | TCP/UDP | DNS |

- **UDP 53** → Standard DNS queries.
- **TCP 53** → Zone transfers (AXFR) and large DNS responses.

---

# DNS Server Types

| Server | Description |
|---------|-------------|
| Root Server | Directs queries to Top-Level Domain (TLD) servers. |
| Authoritative Nameserver | Holds the official records for a DNS zone. |
| Non-authoritative Nameserver | Returns cached or recursively obtained records. |
| Caching Server | Stores DNS responses temporarily to improve performance. |
| Forwarding Server | Forwards DNS requests to another DNS server. |
| Resolver | Performs local name resolution on a host or router. |

---

# Common DNS Records

| Record | Purpose |
|---------|---------|
| **A** | Maps hostname → IPv4 address. |
| **AAAA** | Maps hostname → IPv6 address. |
| **MX** | Specifies mail servers. |
| **NS** | Specifies authoritative name servers. |
| **TXT** | Stores arbitrary text (SPF, DKIM, DMARC, verification records). |
| **CNAME** | Alias pointing to another hostname. |
| **PTR** | Reverse lookup (IP → Hostname). |
| **SOA** | Start of Authority; contains zone administration information. |

---

# Default Configuration (Bind9)

Common configuration files:

```text
/etc/bind/named.conf.local
/etc/bind/named.conf.options
/etc/bind/named.conf.log
```

Typical zone configuration:

```bash
zone "domain.com" {
    type master;
    file "/etc/bind/db.domain.com";
    allow-update { key rndc-key; };
};
```

---

# Zone Files

Zone files define all forward DNS records.

Typical location:

```text
/etc/bind/db.domain.com
```

Contains records such as:

- SOA
- NS
- A
- MX
- CNAME

Example:

```text
server1   IN A      10.129.14.5
server2   IN A      10.129.14.7
www       IN CNAME  server2
ftp       IN CNAME  server1
```

---

# Reverse Lookup Zone

Reverse lookups translate an IP address back into a hostname using **PTR** records.

Typical file:

```text
/etc/bind/db.10.129.14
```

Example:

```text
5   IN PTR server1.domain.com.
```

---

# Important Configuration Options

| Setting | Description |
|----------|-------------|
| allow-query | Hosts allowed to perform DNS queries. |
| allow-recursion | Hosts allowed recursive lookups. |
| allow-transfer | Hosts allowed to perform zone transfers (AXFR). |
| zone-statistics | Enables DNS zone statistics. |

---

# Common Misconfigurations

- Zone transfers enabled for everyone.
- Recursive queries allowed from untrusted hosts.
- DNS version disclosure enabled.
- Internal DNS records publicly accessible.
- Weak access control on `allow-transfer`.
- Overly permissive `allow-query`.

---

# Enumeration

## Nmap

Detect DNS service and enumerate scripts.

```bash
sudo nmap -sV -sC -p53 --script dns* <TARGET>
```

---

## Query A Record

```bash
dig A domain.com @<DNS_SERVER>
```

---

## Query AAAA Record

```bash
dig AAAA domain.com @<DNS_SERVER>
```

---

## Query MX Records

```bash
dig MX domain.com @<DNS_SERVER>
```

---

## Query NS Records

```bash
dig NS domain.com @<DNS_SERVER>
```

---

## Query TXT Records

```bash
dig TXT domain.com @<DNS_SERVER>
```

Useful for discovering:

- SPF
- DKIM
- DMARC
- Domain verification tokens

---

## Query SOA Record

```bash
dig SOA domain.com @<DNS_SERVER>
```

Returns:

- Primary nameserver
- Administrator email
- Serial number
- Refresh interval
- Retry interval
- Expiration
- Minimum TTL

---

## Reverse Lookup (PTR)

```bash
dig -x <IP_ADDRESS> @<DNS_SERVER>
```

Example:

```bash
dig -x 10.129.14.5
```

---

## Query All Available Records

```bash
dig ANY domain.com @<DNS_SERVER>
```

May reveal:

- TXT records
- NS records
- SOA
- Other exposed records

> **Note:** Many modern DNS servers disable `ANY` queries.

---

## Query DNS Version

Some Bind servers disclose their version.

```bash
dig CH TXT version.bind @<DNS_SERVER>
```

Example output:

```text
9.10.6-P1
```

Useful for identifying vulnerable versions.

---

# Zone Transfer (AXFR)

Attempt to retrieve the entire DNS zone.

```bash
dig AXFR domain.com @<DNS_SERVER>
```

If successful, it may expose:

- Internal hosts
- Mail servers
- VPN gateways
- Domain controllers
- Workstations
- Internal IP addresses

Example:

```bash
dig AXFR internal.domain.com @<DNS_SERVER>
```

---

# Subdomain Enumeration

## Manual Brute Force

```bash
for sub in $(cat wordlist.txt); do
    dig $sub.domain.com @<DNS_SERVER> \
    | grep -v ';\|SOA' \
    | sed '/^$/d'
done
```

---

## DNSenum

Automated DNS enumeration.

```bash
dnsenum \
--dnsserver <DNS_SERVER> \
--enum \
-p 0 \
-s 0 \
-f wordlist.txt \
domain.com
```

Capabilities:

- NS enumeration
- MX enumeration
- Zone transfer attempts
- Subdomain brute forcing
- Bind version detection

---

# Enumeration Workflow

1. Discover DNS service on port **53**.
2. Enumerate **NS** records.
3. Retrieve **SOA** record.
4. Query **MX** records.
5. Inspect **TXT** records (SPF, DKIM, DMARC).
6. Attempt **ANY** query.
7. Attempt **version.bind** query.
8. Attempt **AXFR** zone transfer.
9. Enumerate subdomains.
10. Perform reverse lookups on discovered IPs.

---

# Useful Tools

| Tool | Purpose |
|------|---------|
| dig | Manual DNS queries. |
| host | Simple DNS lookup utility. |
| nslookup | Legacy DNS query tool. |
| dnsenum | Automated DNS enumeration. |
| Nmap | DNS detection and NSE scripts. |

---

# Best Practices

- Enumerate **NS**, **MX**, **TXT**, and **SOA** records first.
- Always test for **AXFR** zone transfers.
- Check if `version.bind` is exposed.
- Review TXT records for useful infrastructure information.
- Perform subdomain brute forcing when zone transfer fails.
- Reverse lookup discovered IP addresses.

---

# Key Takeaways

- DNS typically runs on **TCP/UDP port 53**.
- **UDP** handles standard queries; **TCP** is mainly used for **AXFR** zone transfers.
- **SOA**, **NS**, **MX**, and **TXT** records often reveal valuable infrastructure details.
- Misconfigured **AXFR** can expose an entire DNS zone, including internal hosts.
- **TXT** records frequently disclose SPF, DKIM, DMARC, and domain verification data.
- Tools such as **dig**, **dnsenum**, **host**, and **Nmap** are essential for DNS enumeration.
- Always attempt zone transfers before resorting to brute-force subdomain enumeration.