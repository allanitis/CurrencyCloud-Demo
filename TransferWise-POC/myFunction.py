import boto3
import dash

ddb = boto3.client("dynamodb")
try:
    data = ddb.get_item(
        TableName='myNewDataTable',
        Key={'name':{'S':'matt'}}
    )
except BaseException as e:
    print(e)
    raise(e)
