# Linux Notes

```bash
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