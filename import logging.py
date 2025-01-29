import logging
import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def send_to_discord(icmp_status, ip_info):
    webhook_url = 'https://discord.com/api/webhooks/1310157589849313290/nfxCGmXfb0WMoZoNDbnIlxmyNM4VqQQh-VQfFo4fIHh6bwnV1xVu0WCK1j9Vfm0-Y5N4'
    discord_message = {
        "content": "IP Information",
        "embeds": [{
            "title": "ICMP Status",
            "fields": [
                {"name": "IP Address", "value": ip_info['ip']},
                {"name": "ICMP Status", "value": icmp_status}
            ]
        }]
    }
    logging.debug(f"Sending message to Discord: {discord_message}")
    response = requests.post(webhook_url, json=discord_message)
    if response.status_code == 200:
        logging.debug("Webhook sent successfully.")
    else:
        logging.error(f"Error sending webhook: {response.status_code}")
