import aws_cdk as core
import aws_cdk.assertions as assertions

from mqtt_dynamodb_stack import MqttDynamodbStack

def test_sqs_queue_created():
    app = core.App()
    stack = MqttDynamodbStack(app, "MqttDynamodbStack")
    template = assertions.Template.from_stack(stack)

