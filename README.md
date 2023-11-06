# Web-applicatin Vulnerability Scanner (WAVS)

**Introduction:**

The Website Vulnerability Scanner is a powerful open-source tool designed for comprehensive web application security assessments. It combines network mapping, port scanning, and web application vulnerability detection to provide users with a holistic view of their web assets' security posture.

**How It Works:**

The scanner integrates multiple open-source tools, including Nmap, Wapiti, Gobuster, and Nuclei, to perform a variety of scans. Here's how it works:

1. **Quick Scan:** This option rapidly identifies open ports and services using Nmap and checks for common web vulnerabilities with Wapiti.

2. **Full Scan:** For in-depth analysis, the full scan employs Gobuster for directory and file brute-forcing, and Nuclei to find potential web application security issues.

3. **Result Handling:** Scan results are conveniently presented through the web interface, allowing users to view detailed reports.



**How to Use:**

Getting started with the Website Vulnerability Scanner is easy:

1. **Access the Scanner:** Download and install requirements using "pip install -r requirements.txt" command and install the required tools manually....list given below...once that is done goto the "site" and run "python3.9 scan.py"....go to the localhost:5000 ....done

2. **Input Target URL:** Enter the URL or IP address you want to scan.

3. **Choose Scan Type:** Select either a Quick Scan or Full Scan based on your assessment needs.

4. **View Results:** Explore the scan results to identify vulnerabilities and security issues in your web applications.




Feel free to explore the scanner's capabilities, contribute to its development, and enhance your web application security.

**Project Status:**

This project is actively maintained and open to contributions. We welcome your feedback and involvement to make web applications more secure.




#list of tools?
#nmap
#wapiti
#gobuster
#nuclei


#how to install tools?

# For Debian-based systems (install separately)
	#sudo apt-get install nmap
	#sudo apt-get install wapiti
	#sudo apt-get install gobuster
	#sudo apt-get install nuclei

# For MacOS (install separately)
	#brew install nmap
	#brew install wapiti
	#brew install gobuster
	#brew install nuclei
