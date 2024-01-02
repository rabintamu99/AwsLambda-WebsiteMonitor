import boto3
import requests
import json

slack_webhook_url = "slack_webhook_url"

websites_to_check = [
    "https://example.com"
]

def lambda_handler(event, context):
    for website in websites_to_check:
        check_website(website)

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"{url} is online. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"{url} is offline. Error: {str(e)}")
        send_slack_alert(url, str(e))

def send_slack_alert(website_url, error_message):
    message = {
        "text": f"Alert: Website {website_url} is offline!\nError: {error_message}"
    }

    # Make a POST request to the Slack incoming webhook URL
    response = requests.post(slack_webhook_url, json=message)

    # Log the response
    print(response.text)
