import requests
from ping3 import ping

# ICMP Check function
def check_icmp(ip):
    response = ping(ip)
    if response is None:
        return "Failed"
    else:
        return "Alive"

# Geolocation lookup function
def get_ip_geolocation(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "IP Address": data.get("ip"),
            "City": data.get("city"),
            "State": data.get("region"),
            "Country": data.get("country"),
            "Organization": data.get("org"),
            "ASN Name": data.get("asn"),
            "VPN": "No",  # Adjust based on any additional checks you might want to perform
            "Proxy": "No",  # Same for proxy checks
            "TOR": "No"  # Same for TOR detection
        }
    else:
        return {"error": "Could not retrieve data"}

# Webhook function
def send_to_webhook(data, webhook_url):
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print("Successfully sent data to webhook")
        else:
            print(f"Failed to send data, status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to webhook: {e}")

# Main function
def main():
    ip = "104.28.55.229"  # Replace with the target IP address
    webhook_url = "YOUR_WEBHOOK_URL"  # Replace with your actual webhook URL

    # Check ICMP
    icmp_status = check_icmp(ip)

    # Get IP geolocation data
    geolocation_data = get_ip_geolocation(ip)

    # Add ICMP status to the data
    geolocation_data["Received ICMP"] = icmp_status

    # Send the data to the webhook
    send_to_webhook(geolocation_data, webhook_url)

# Run the script
if __name__ == "__main__":
    main()