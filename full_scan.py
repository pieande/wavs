import subprocess
import os
from urllib.parse import urlparse

def gobuster_scan(url):
    # Remove the protocol part of the URL
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    # Run gobuster scan and save results to file
    gobuster_result = subprocess.run(["gobuster", "dir", "-u", hostname, "-w", "/usr/share/wordlists/dirb/common.txt", "-b","404,403"], capture_output=True, text=True)

    # Extract essential information from gobuster output
    output_lines = gobuster_result.stdout.splitlines()
    essential_info = []
    for line in output_lines:
        if "Status: 200" in line:  # Assuming we're interested in successful finds
            essential_info.append(line)

    # Save gobuster results to a dynamically generated file
    gobuster_results_dir = "gobuster_results"
    os.makedirs(f"static/{gobuster_results_dir}", exist_ok=True)
    gobuster_filename = os.path.join(gobuster_results_dir, f"{hostname}.txt")
    with open(f"static/{gobuster_filename}", "w") as f:
        f.write(gobuster_result.stdout)

    # Print gobuster output and error messages for debugging
    print(gobuster_result.stdout)
    print(gobuster_result.stderr)

    return essential_info, gobuster_filename
    
def nuclei_scan(url):
    # Remove the protocol part of the URL
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    # Run nuclei scan and save results to file
    nuclei_result = subprocess.run(["nuclei", "-u", hostname, "-t", "/home/kali/nuclei-templates"], capture_output=True, text=True)

    # Extract essential information from nuclei output
    output_lines = nuclei_result.stdout.splitlines()
    essential_info = []
    for line in output_lines:
        if "severity: high" in line:  # Assuming we're interested in high severity findings
            essential_info.append(line)

    # Save nuclei results to a dynamically generated file
    nuclei_results_dir = "nuclei_results"
    os.makedirs(f"static/{nuclei_results_dir}", exist_ok=True)
    nuclei_filename = os.path.join(nuclei_results_dir, f"{hostname}.txt")
    with open(f"static/{nuclei_filename}", "w") as f:
        f.write(nuclei_result.stdout)

    # Print nuclei output and error messages for debugging
    print(nuclei_result.stdout)
    print(nuclei_result.stderr)

    return essential_info, nuclei_filename

def perform_scans(url):
   gobuster_info, gobuster_file = gobuster_scan(url)
   nuclei_info, nuclei_file = nuclei_scan(url)
   return {"gobuster": (gobuster_info, gobuster_file), "nuclei": (nuclei_info, nuclei_file)}