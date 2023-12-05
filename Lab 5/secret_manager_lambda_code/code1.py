import json
import boto3

def lambda_handler(event, context):
    # Input values
    Table_name = 'Employee_table1'
    AWS_Access_Key = 'Copy Aceess Key Here'
    AWS_Secret_Access_Key = 'Copy Secret Access Key Here'
    
    # Create a DynamoDB table
    print('DynamoDB Table creation started.')
    
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id = AWS_Access_Key,
        aws_secret_access_key = AWS_Secret_Access_Key,
        region_name = 'us-east-1'
    )
    
    Employee_table = dynamodb.create_table(
        TableName = Table_name,
        KeySchema = [
            {
                'KeyType': 'HASH',
                'AttributeName': 'EmpId'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'EmpId',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    )
    
    
    
    
    # Wait until the Table gets created
    Employee_table.meta.client.get_waiter('table_exists').wait(TableName = Table_name)
    print('DynamoDB Table Creation Completed.')
    
    print('Insert Employee data to table started.')
    # Insert 1st item into DynamoDB table
    table = dynamodb.Table(Table_name)
    table.put_item(
    Item = {
            'EmpId': 100,
            'FirstName': 'Harry',
            'LastName': 'Styles',
            'Dept': 'IT',
            'Age': 28
        }
    )
    
    
    
    # Insert 2nd item into DynamoDB table
    table.put_item(
    Item = {
            'EmpId': 200,
            'FirstName': 'Sam',
            'LastName': 'Billings',
            'Dept': 'BE',
            'Age': 22
        }
    )
    
    
    
    # Insert 3rd item into DynamoDB table
    table.put_item(
    Item = {
            'EmpId': 300,
            'FirstName': 'Pete',
            'LastName': 'Davidson',
            'Dept': 'EE',
            'Age': 25
        }
    )
    print('Insert Employee data to table Completed.')