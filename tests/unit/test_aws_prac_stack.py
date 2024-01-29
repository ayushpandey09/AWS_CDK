import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_prac.aws_prac_stack import AwsPracStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_prac/aws_prac_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsPracStack(app, "aws-prac")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
