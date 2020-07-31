from botocore.vendored import requests
import boto3
import dash

ddb = boto3.client("dynamodb")
try:
    data = ddb.get_item(
        TableName='myNewDataTable',
        Key={'name':{'S':'matt'}}
    try:
        res = requests.get(
            "https://api.sandbox.transferwise.tech/v1/rates",
            params={"source":"usd"},
            headers={"Accept":"application/json"}
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        raise(e)
    )
except BaseException as e:
    print(e)
    raise(e)
