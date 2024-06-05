import aws_cdk as core
import aws_cdk.assertions as assertions

from mqtt.mqtt_dynamodb_stack import MqttDynamoDBStack

def test_sqs_queue_created():
    app = core.App()
    stack = MqttDynamoDBStack(app, "MqttDynamoDBStack")
    template = assertions.Template.from_stack(stack)

