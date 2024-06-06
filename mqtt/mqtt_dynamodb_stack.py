from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class MqttDynamoDBStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "VPC", max_azs=2)

        # Create a security group for EC2 instance
        security_group = ec2.SecurityGroup(
            self, "EC2SecurityGroup",
            vpc=vpc,
            description="Allow SSH and MQTT traffic",
            allow_all_outbound=True
        )
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "allow SSH access"
        )
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(1883), "allow MQTT access"
        )

        # Create EC2 instance
        instance = ec2.Instance(
            self, "MQTTInstance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            security_group=security_group,
            key_name="crypto_stream", 
        )

        # Add user data script to install Mosquitto
        instance.add_user_data(
            "#!/bin/bash",
            "sudo yum update -y",
            "sudo amazon-linux-extras install epel -y",
            "sudo yum install mosquitto -y",
            "sudo systemctl start mosquitto",
            "sudo systemctl enable mosquitto"
        )

        # Create DynamoDB table
        table = dynamodb.Table(
            self, "SensorDataTable",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="timestamp", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # IAM Role for EC2 to interact with DynamoDB
        role = iam.Role(
            self, "EC2DynamoDBRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess")
        )

        # Attach the role to the EC2 instance
        instance.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:*"],
                resources=[table.table_arn]
            )
        )
        instance.role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess")
        )


