from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigateway
    # aws_sqs as sqs,
)
from constructs import Construct

class AwsPracStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        table = dynamodb.TableV2(self, "TaskTableDynamoDb",
            partition_key=dynamodb.Attribute(name="taskId", type=dynamodb.AttributeType.STRING)
        )
    
        create_task_lambda = _lambda.Function(self, "TaskTable",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="create-task.lambda_handler",
            code=_lambda.Code.from_asset('lambda-functions')
        )
    
        api = apigateway.RestApi(self,'TaskApi')
    
        tasks_resource = api.root.add_resource('tasks')
        tasks_resource.add_method('POST', apigateway.LambdaIntegration(create_task_lambda))
        
        
    
       
