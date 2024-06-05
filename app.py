#!/usr/bin/env python3
import os

import aws_cdk as cdk

from mqtt_dynamodb_stack import MqttDynamodbStack


app = cdk.App()

MqttDynamodbStack(app, "MqttDynamodbStack")

app.synth()
