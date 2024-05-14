from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# Set up Chrome options (remove headless for testing)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage
chrome_options.add_argument("--start-maximized")  # Start Chrome maximized

# Set up ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

@app.route('/get_visuals', methods=['GET'])
def get_visuals():
    try:
        # Get report ID from query parameters
        report_id = request.args.get('report_id')

        # Construct the Power BI report URL
        report_url = f'https://app.powerbi.com/groups/b0ae7a1c-44b0-4581-bbf7-e63b9e5ffb4a/reports/6e3243a2-6cbf-44e7-9eaa-78f150d44fe8/ReportSection?ctid=b9edde28-a188-4c9d-9f55-621432f7f11d&pbi_source=shareVisual&visual=7354c3aba991dcd80b19&height=272.60&width=706.55&bookmarkGuid=99b2d21d-b7e5-4ab3-b168-1270d195081a'

        # Navigate to the Power BI report
        driver.get(report_url)

        # Wait for the page to load (you may need to adjust the wait time)
        driver.implicitly_wait(10)

        # Capture the screenshot (use PNG format)
        screenshot = driver.get_screenshot_as_png()

        # Save the screenshot as an image file (you can modify the filename)
        with open('power_bi_visual.png', 'wb') as f:
            f.write(screenshot)

        return jsonify({"message": "Visual captured successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
