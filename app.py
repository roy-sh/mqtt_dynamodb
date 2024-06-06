#!/usr/bin/env python3
import os

import aws_cdk as cdk

from mqtt.mqtt_dynamodb_stack import MqttDynamoDBStack


app = cdk.App()

MqttDynamoDBStack(app, "MqttDynamoDBStack")

app.synth()
