# AwsLambda-WebsiteMonitor

This project contains a Python script for monitoring the availability of websites and sending alerts to Slack. It uses AWS Lambda for running the script in a serverless environment.

## Getting Started

These instructions will guide you on how to set up and run the Website Monitor on your own AWS environment.

### Prerequisites

- AWS account with access to Lambda, CloudWatch
- Python 3.x
- `requests` library for Python
- Slack account and a configured incoming webhook

### Setup

1. **AWS Lambda Function**:
   - Create a new Lambda function in your AWS Console.
   - Set the runtime to Python 3.x.

2. **Environment Variables**:
   - Set `SLACK_WEBHOOK_URL` as an environment variable in the Lambda configuration to store your Slack webhook URL securely.

3. **Deployment Package**:
   - Zip your Python script along with any dependencies.
   - Upload the zip file to your Lambda function.

4. **Execution Role**:
   - Ensure the Lambda function has an execution role with necessary permissions.

5. **Schedule**:
   - Use AWS CloudWatch Events to trigger the Lambda function at your desired frequency.

### Installing Dependencies

Use pip to install necessary Python packages:

