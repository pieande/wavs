// JavaScript for handling scan button clicks and sending requests

    // Function to send a scan request to the Python script
    function sendScanRequest(scanType) {
      const url = document.getElementById('urlInput').value; // Get the IP address input value
      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/scan', true); // Update the URL to '/scan'
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          console.log(xhr.responseText); // Log the response from the Python script
        }
      };
      const formData = `scanType=${scanType}&ipAddress=${encodeURIComponent(url)}`;
      xhr.send(formData);
    }
    // Attach event listeners to the scan buttons
    const quickScanBtn = document.getElementById('quickScanBtn');
    quickScanBtn.addEventListener('click', function () {
      sendScanRequest('quick'); // Send quick scan request
      this.classList.toggle('green-bg'); // Toggle green background on button
    });
    const fullScanBtn = document.getElementById('fullScanBtn');
    fullScanBtn.addEventListener('click', function () {
      sendScanRequest('full'); // Send full scan request
      this.classList.toggle('green-bg'); // Toggle green background on button
    });
