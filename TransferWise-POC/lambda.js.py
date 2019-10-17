import boto3
ddb = boto3.client("dynamodb")
try:
    data = ddb.get_item(
        TableName='myTable',
        Key={'sietnrsient':{'S':'myPartitionKey'}}
    )
except BaseException as e:
    print(e)
    raise(e)
