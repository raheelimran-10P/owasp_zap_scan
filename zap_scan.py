import time
from zapv2 import ZAPv2

# Configuration
target_url = ''  # Replace with your target URL
api_key = ''  # Replace with your ZAP API key
zap_proxy = ''  # Default ZAP proxy

# Initialize ZAP API
zap = ZAPv2(apikey=api_key, proxies={'http': zap_proxy, 'https': zap_proxy})


def start_passive_scan():
    print('Starting passive scan...')
    zap.urlopen(target_url)  # Access target URL
    time.sleep(2)  # Wait for the passive scan to complete


def start_active_scan():
    print('Starting active scan...')
    scan_id = zap.ascan.scan(target_url)
    while int(zap.ascan.status(scan_id)) < 100:
        print(f'Scan progress: {zap.ascan.status(scan_id)}%')
        time.sleep(5)
    print('Active scan completed.')


def generate_html_report(output_file):
    print('Generating HTML report...')
    report_html = zap.core.htmlreport()
    with open(output_file, 'w') as file:
        file.write(report_html)
    print(f'Report saved as {output_file}')


# Run scans
start_passive_scan()
start_active_scan()

# Generate report
output_file = 'zap_scan_report.html'  # Define the output file name
generate_html_report(output_file)
