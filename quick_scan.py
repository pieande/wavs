import subprocess
import os
from urllib.parse import urlparse

def quick_scan(ipAddress):
    # Remove the protocol part of the URL
    parsed_url = urlparse(ipAddress)
    hostname = parsed_url.hostname
    
    # Run nmap scan and save results to file
    nmap_result = subprocess.run(["nmap", hostname], capture_output=True, text=True)
    
    # Extract essential information from nmap output
    output_lines = nmap_result.stdout.splitlines()
    essential_info = []
    for line in output_lines:
        if "open" in line:
            essential_info.append(line)
    
    # Save nmap results to a dynamically generated file
    nmap_results_dir = "nmap_results"
    os.makedirs(f"static/{nmap_results_dir}", exist_ok=True)
    nmap_filename = os.path.join(nmap_results_dir, f"{hostname}.txt")
    with open(f"static/{nmap_filename}", "w") as f:
        f.write(nmap_result.stdout)
    
    # Print nmap output and error messages for debugging
    print(nmap_result.stdout)
    print(nmap_result.stderr)
    
    # Run wapiti scan
    wapiti_result = subprocess.run(["wapiti", "-u", ipAddress, "-o", "static/wapiti_results"], capture_output=True, text=True)
    
    # Print any error messages from the wapiti scan
    print(wapiti_result.stderr)
    
    # Get the name of the wapiti results file
    wapiti_results_dir = "static/wapiti_results"  # Remove extra indentation from this line
    wapiti_filename = None
    for filename in os.listdir(wapiti_results_dir):
        if filename.endswith(".html"):
            wapiti_filename = os.path.join("wapiti_results", filename)
            break
    
    return essential_info, wapiti_filename, nmap_filename
