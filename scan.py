# modified script.py

from flask import Flask, request, render_template

from quick_scan import quick_scan
from full_scan import gobuster_scan, nuclei_scan  # import nuclei_scan from full_scan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    if request.method == 'POST':
        ipAddress = request.form['ipAddress']
        scan_type = request.form['scanType']

        if scan_type == 'quick':
            essential_info, wapiti_filename, nmap_filename = quick_scan(ipAddress)
            if wapiti_filename:
                return render_template('scan_result.html',essential_info=essential_info,wapiti_filename=wapiti_filename,nmap_filename=nmap_filename)
            else:
                return "Error: Could not find wapiti results file"

        elif scan_type == 'full':
            essential_info, gobuster_filename = gobuster_scan(ipAddress)  # run gobuster scan
            if not gobuster_filename:  # check if gobuster_filename exists
                return "Error: Could not find gobuster results file"
            
            nuclei_info, nuclei_filename = nuclei_scan(ipAddress)  # run nuclei scan
            if not nuclei_filename:  # check if nuclei_filename exists
                return "Error: Could not find nuclei results file"
            
            return render_template('full_scan_result.html',essential_info=essential_info,gobuster_filename=gobuster_filename, nuclei_info=nuclei_info, nuclei_filename=nuclei_filename)  # add nuclei_filename to the template


if __name__ == '__main__':
    app.run()
