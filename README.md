# extract-ips-and-interrogate-IPINFO
This script detects all .CSV files from a folder, parses them and extracts all IPs from the .CSV files. Then, it interrogates ipinfo.io and extracts useful information about those IPs. 

Scenario: 
We received reports regarding hundreds of IPs which were identified as potentially malicious agents. This script parses the reports and automatically gathers publicly available information (OSINT) about those IPs and generates a .CSV file.

Modules needed:
ipinfo, glob

Usage:
In main.py modify the "access_token" in the main function and introduce the one you have received when you registered to ipinfo.io

