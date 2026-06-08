# Linux Notes

sudo -l                                         # Check sudo permissions
ss -tulpn                                       # Show listening ports/services
lsof -i                                         # Network-related processes
ps auxf                                         # Process tree
crontab -l                                      # Current user cron jobs
cat /etc/crontab                                # System cron jobs
grep -Ri "password" /home 2>/dev/null           # Search for passwords
find / -name "*.log" 2>/dev/null                # Find log files
uname -a                                        # Kernel/system info
hostnamectl                                     # Detailed host info
ip route                                        # Routing table
arp -a                                          # ARP cache
python3 -m http.server 8000                     # Quick HTTP server
nc -lvnp 4444                                   # Netcat listener
wget http://IP/file                             # Download file
curl http://IP/file -o file                     # Download with curl
chmod +x file                                   # Make executable
strings file                                    # Extract readable strings
file binary                                     # Identify file type


# Nmap Notes

nmap -p- --min-rate 10000 "IP"                    # Fast full port scan
nmap -sC -sV "IP"                                 # Default scripts + versions
nmap -A "IP"                                      # Aggressive scan
nmap -Pn "IP"                                     # Skip host discovery
nmap -sU "IP"                                     # UDP scan
nmap --script vuln "IP"                           # Vulnerability scripts
nmap --script smb-enum-shares -p445 "IP"          # Enumerate SMB shares
nmap --script smb-os-discovery -p445 "IP"         # SMB OS discovery
nmap --script ftp-anon -p21 "IP"                  # Anonymous FTP check
nmap --script http-title "IP"                     # Get webpage title
nmap --script http-enum "IP"                      # Enumerate web directories
nmap --script ssl-cert -p443 "IP"                 # SSL certificate info
nmap -sT "IP"                                     # TCP connect scan
nmap -O "IP"                                      # OS detection
nmap -sS "IP"                                     # SYN stealth scan
nmap -p 80,443,21,22 "IP"                         # Specific ports
nmap -oN scan.txt "IP"                            # Save output
nmap -T4 "IP"                                     # Faster scan timing
nmap -sC -sV -p- -T4 "IP"                         # Common HTB enumeration scan
sudo nmap -sn 192.168.1.0/24                      # Discover active hosts on the local network.