import aws_cdk as core
import aws_cdk.assertions as assertions

from mqtt_dynamodb.mqtt_dynamodb_stack import MqttDynamodbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in mqtt_dynamodb/mqtt_dynamodb_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MqttDynamodbStack(app, "mqtt-dynamodb")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
