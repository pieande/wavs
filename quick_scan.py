import subprocess
import os
from urllib.parse import urlparse
import time
import threading



# Function to delete a file
def delete_file(path):
    # Check if the file exists
    if os.path.exists(path):
        # If it exists, remove it
        os.remove(path)
        # Print a message indicating the file has been deleted
        print(f"The file {path} has been deleted.")

def quick_scan(ipAddress):
    # Parse the IP address to get the hostname
    parsed_url = urlparse(ipAddress)
    hostname = parsed_url.hostname

    # Run nmap scan and capture the output
    nmap_result = subprocess.run(["nmap", hostname], capture_output=True, text=True)

    # Split the output into lines
    output_lines = nmap_result.stdout.splitlines()

    # Initialize a list to store the essential information
    essential_info = []

    # Loop through each line in the output
    for line in output_lines:
        # If the line contains "open", add it to the essential info list
        if "open" in line:
            essential_info.append(line)

    # Create a directory to store the nmap results
    nmap_results_dir = "nmap_results"
    os.makedirs(f"static/{nmap_results_dir}", exist_ok=True)

    # Create a filename for the nmap results
    nmap_filename = os.path.join(nmap_results_dir, f"{hostname}.txt")

    # Open the file and write the nmap results to it
    with open(f"static/{nmap_filename}", "w") as f:
        f.write(nmap_result.stdout)

    # Print the nmap output and error messages for debugging
    print(nmap_result.stdout)
    print(nmap_result.stderr)

    # Run wapiti scan and capture the output
    wapiti_result = subprocess.run(["wapiti", "-u", ipAddress, "-o", "static/wapiti_results"], capture_output=True, text=True)

    # Print any error messages from the wapiti scan
    print(wapiti_result.stderr)

    # Initialize a variable to store the name of the wapiti results file
    wapiti_results_dir = "static/wapiti_results"
    wapiti_filename = None

    # Loop through each file in the wapiti results directory
    for filename in os.listdir(wapiti_results_dir):
        # If the file ends with ".html", set it as the wapiti filename and break the loop
        if filename.endswith(".html"):
            wapiti_filename = os.path.join("wapiti_results", filename)
            break

   

    # Schedule the deletion of the nmap results file after 2 minutes
    threading.Timer(120, delete_file, args=[f"static/{nmap_filename}"]).start()

    # Schedule the deletion of the wapiti results file after 2 minutes
    threading.Timer(120, delete_file, args=[f"static/{wapiti_filename}"]).start()

    # Return the essential info, wapiti filename, and nmap filename
    return essential_info, wapiti_filename, nmap_filename
