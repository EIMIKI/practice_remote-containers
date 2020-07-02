import boto3
import os

def create_log_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://dynamo:8000")

    table = dynamodb.create_table(
        TableName='Logs',
        KeySchema=[
            {
                'AttributeName': 'time',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'time',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table


if __name__ == '__main__':
    log_table = create_log_table()
    print("Table status:", log_table.table_status)
