import json
import os
import uuid
import boto3

task_table_name = os.environ['TASK_TABLE_NAME']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(task_table_name)

def lambda_handler(event,context):
    reqest_body = json.loads(event['body'])
    
    task_id = str(uuid.uuid4())
    
    task_title = reqest_body.get('title','')
    task_description = reqest_body.get('description','')
    task_status = reqest_body.get('status','pending')
    
    table.put_item(
        Item={
            'taskId' : task_id,
            'title' : task_title,
            'description' : task_description,
            'status' : task_status
        }
    )
    
    response = {
        'statusCode': 200,
        'body': json.dumps({'taskId': task_id}),
        'headers': {'Content-Type': 'application/json'}
    }

    return response