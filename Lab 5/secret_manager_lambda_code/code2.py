import json
import boto3

def lambda_handler(event, context):
	# Input values
	Table_name = 'Employee_table1'
	AWS_Access_Key = ''
	AWS_Secret_Access_Key = ''

	# Create a DynamoDB table
	print('DynamoDB Table creation started.')
 
	dynamodb = boto3.resource(
		'dynamodb',
		aws_access_key_id = AWS_Access_Key,
    	          aws_secret_access_key = AWS_Secret_Access_Key,
		region_name = 'us-east-1'
	)

	# Connect to table & Scan the entire table
	table = dynamodb.Table(Table_name)
	response = table.scan()

	print('---------------------------------------')
	print('------------Employee DETAILS------------')
	print('---------------------------------------')
	for item in response['Items']:
		print('Employee Id : ', item['StudId'])
		print('Employee Name : ', item['FirstName'], ' ', item['LastName'])
		print('Employee Department : ', item['Dept'])
		print('Employee Age : ', item['Age'])
		print('_______________________________')
	print('---------------------------------------')