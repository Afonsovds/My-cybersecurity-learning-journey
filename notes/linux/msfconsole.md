# Metasploit (msfconsole)


search type:exploit name:ms17_010     # Search exploits by name
search platform:windows               # Filter by operating system
search cve:2021-44228                # Search by CVE vulnerability

info                                  # Show detailed module information
show options                          # Show required and configurable options
show payloads                         # List compatible payloads
show targets                          # List supported targets
show missing                          # Show missing required configuration

check                                 # Check if the target is vulnerable (if supported)
exploit -j                            # Run exploit as a background job
exploit -z                            # Do not automatically interact with session

sysinfo                               # Show target system information
getuid                                # Show current user on target
ps                                    # List running processes
migrate <pid>                         # Move to another process
hashdump                              # Dump password hashes (if privileged)
screenshot                            # Take a screenshot of the target