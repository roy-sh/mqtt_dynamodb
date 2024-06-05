# Real-Time Mobile Logger with AWS CDK Deployment

This project sets up a real-time mobile logger that sends sensor data to an HTTP endpoint, stores the data in a DynamoDB table, and uses an MQTT server for message brokering. The infrastructure is provisioned using AWS CDK, and the deployment is automated through GitHub Actions.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Deployment](#deployment)
- [Usage](#usage)
- [Development](#development)
- [License](#license)

## Prerequisites

- AWS Account
- AWS CLI configured with your credentials
- Node.js and npm
- Python 3.9 or later
- AWS CDK CLI
- GitHub account for CI/CD integration

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/real-time-mobile-logger.git
cd real-time-mobile-logger
```

### 2. Install Dependencies

```sh
npm install -g aws-cdk
pip install -r requirements.txt
```

### 3. Configure AWS Credentials
Ensure your AWS CLI is configured with the necessary credentials:

```sh
aws configure
```
### 4. Initialize CDK Project
If you haven't already, initialize your CDK project:

```sh
cdk init app --language python
```

## Deployment

### 1. Create Key Pair
Create an EC2 key pair to use with your instances:

```sh
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem
chmod 400 MyKeyPair.pem
```

### 2. Add AWS Credentials to GitHub Secrets
In your GitHub repository, go to Settings > Secrets and variables > Actions and add the following secrets:

```sh
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

### 3. GitHub Actions Workflow
The GitHub Actions workflow (.github/workflows/deploy.yml) will handle the deployment. It will:

- Checkout the code
- Set up Python and Node.js environments
- Install dependencies
- Configure AWS credentials
- Deploy the CDK stack

### 4. Deploy Manually
You can also deploy the stack manually using the CDK CLI:

```sh
cdk deploy
```

## Usage
### Sending Data
Your mobile app should send sensor data in batches to the HTTP endpoint provided by your EC2 instance.

### Retrieving Data
The data will be stored in the DynamoDB table specified in your CDK stack. You can query this table using the AWS Management Console, AWS CLI, or SDKs.

## Development
### Local Development

- To run the Flask server locally:

1. Start the Flask server:

```sh
export FLASK_APP=app.py
flask run
```
2. Your server will be available at http://localhost:5000/sensor-data.

## Testing
To test the HTTP endpoint, you can use tools like curl or Postman:

```sh
curl -X POST http://localhost:5000/sensor-data -H "Content-Type: application/json" -d '{"sensor": "data"}'
```

## Updating the CDK Stack
Make changes to your CDK stack definitions in cdk_stack.py. To deploy changes:

```
cdk deploy
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.


This `README.md` provides a clear and structured guide for setting up, deploying, and using your project. Make sure to adjust any placeholder values such as repository URLs and usernames.
